import { PROJECTS } from './projects.js';

const root = document.documentElement;
const themeButton = document.querySelector('.theme-toggle');
const storageKey = 'mateo-portfolio-theme-v2';
const stored = localStorage.getItem(storageKey);
root.dataset.theme = stored || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');

function syncTheme() {
  const light = root.dataset.theme === 'light';
  themeButton.textContent = light ? '◒' : '◐';
  themeButton.setAttribute('aria-pressed', String(light));
  themeButton.setAttribute('aria-label', `Switch to ${light ? 'dark' : 'light'} theme`);
}

themeButton.addEventListener('click', () => {
  root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
  localStorage.setItem(storageKey, root.dataset.theme);
  syncTheme();
});
syncTheme();

const links = (project) => `<div class="project-links"><a class="project-demo" href="https://mateotrucco.github.io/${project.slug}/">Open live project <span>↗</span></a><a href="https://github.com/MateoTrucco/${project.slug}">Source</a></div>`;
const preview = (project) => `<div class="project-preview" style="--project-hue:${PROJECTS.indexOf(project) * 24 + 130}"><img src="static/previews/${project.slug}.png" alt="${project.title} interface preview" loading="lazy"><span class="preview-fallback">${project.mark}</span></div>`;

document.querySelector('#featuredProjects').innerHTML = PROJECTS.filter((project) => project.featured).map((project, index) => `<article class="case-card ${index < 2 ? 'case-card-large' : ''}">${preview(project)}<div class="case-body"><div class="project-meta"><span>${project.label}</span><span>${project.tech[0]}</span></div><h3>${project.title}</h3><p>${project.description}</p><div class="proof"><span>What it demonstrates</span><strong>${project.proof}</strong></div>${links(project)}</div></article>`).join('');

const projectGrid = document.querySelector('#projectGrid');
projectGrid.innerHTML = PROJECTS.map((project) => `<article class="project-card" data-slug="${project.slug}" data-category="${project.category}" data-featured="${project.featured}" data-search="${[project.title, project.description, project.label, ...project.tech].join(' ').toLowerCase()}">${preview(project)}<div class="project-body"><div class="project-meta"><span>${project.label}</span><span>${project.tech.join(' · ')}</span></div><h3>${project.title}</h3><p>${project.description}</p><small>${project.proof}</small>${links(project)}</div></article>`).join('');

for (const image of document.querySelectorAll('.project-preview img')) image.addEventListener('error', () => image.hidden = true);

let activeFilter = 'all';
const search = document.querySelector('#projectSearch');
const filterButtons = [...document.querySelectorAll('[data-filter]')];

function filterProjects() {
  const query = search.value.trim().toLowerCase();
  let visible = 0;
  for (const card of projectGrid.children) {
    const categoryMatch = activeFilter === 'all' || card.dataset.category === activeFilter || (activeFilter === 'featured' && card.dataset.featured === 'true');
    const searchMatch = !query || card.dataset.search.includes(query);
    card.hidden = !(categoryMatch && searchMatch);
    if (!card.hidden) visible += 1;
  }
  document.querySelector('#projectCount').textContent = `${visible} project${visible === 1 ? '' : 's'}`;
  document.querySelector('#emptyState').hidden = visible !== 0;
}

for (const button of filterButtons) button.addEventListener('click', () => {
  activeFilter = button.dataset.filter;
  for (const item of filterButtons) {
    const active = item === button;
    item.classList.toggle('is-active', active);
    item.setAttribute('aria-pressed', String(active));
  }
  filterProjects();
});
search.addEventListener('input', filterProjects);
document.querySelector('#year').textContent = new Date().getFullYear();
filterProjects();
