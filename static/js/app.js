import { PROJECTS } from "./projects.js";
const root = document.documentElement,
  THEME = "mateo-ui-theme",
  LANG = "mateo-ui-language";
let language =
    localStorage.getItem(LANG) ||
    (navigator.language.toLowerCase().startsWith("es") ? "es" : "en"),
  activeFilter = "all";
const $ = (s) => document.querySelector(s),
  text = (value) => (typeof value === "string" ? value : value[language]);
const words = {
  en: [
    "useful systems.",
    "clear workflows.",
    "testable ideas.",
    "honest interfaces.",
  ],
  es: [
    "sistemas útiles.",
    "flujos claros.",
    "ideas testeables.",
    "interfaces honestas.",
  ],
};
const terminal = {
  en: [
    [
      "$ portfolio audit --focus",
      "✓ repeated exercises consolidated",
      "✓ real workflows exposed",
      "✓ limitations documented",
      "→ nine projects worth opening",
    ],
    [
      "$ run tests --all",
      "✓ rules engines",
      "✓ permissions & transitions",
      "✓ edge cases",
      "→ confidence is built, not claimed",
    ],
    [
      "$ inspect approach",
      "model → interface → failure states",
      "test → observe → refine",
      "→ curiosity, made concrete",
    ],
  ],
  es: [
    [
      "$ portfolio auditar --enfoque",
      "✓ ejercicios repetidos consolidados",
      "✓ flujos reales expuestos",
      "✓ límites documentados",
      "→ nueve proyectos que vale abrir",
    ],
    [
      "$ ejecutar pruebas --todas",
      "✓ motores de reglas",
      "✓ permisos y transiciones",
      "✓ casos límite",
      "→ la confianza se construye",
    ],
    [
      "$ inspeccionar enfoque",
      "modelo → interfaz → errores",
      "probar → observar → mejorar",
      "→ curiosidad hecha concreta",
    ],
  ],
};
let wordIndex = Math.floor(Math.random() * words[language].length),
  terminalIndex = Math.floor(Math.random() * terminal[language].length);
function visual(project) {
  const content = {
    workflow: "<i></i><i></i><i></i><b>→</b>",
    diagnostics: "<em>84</em><i></i><i></i><i></i>",
    distribution: "<i></i><i></i><i></i><i></i><i></i><i></i>",
    cards: "<b>A♠</b><b>K♥</b><b>Q♣</b>",
    puzzle:
      "<b>1</b><b>2</b><b>3</b><b>4</b><b>5</b><b>6</b><b>7</b><b>8</b><b></b>",
    economy: "<em>+12.4/s</em><i></i><i></i><i></i><i></i>",
    package: "<b>.py</b><i>→</i><b>.exe</b>",
    text: "<b>q onda</b><i>→</i><b>qué tal</b>",
    braille: "<i></i><i></i><i></i><i></i><i></i><i></i>",
  }[project.visual];
  return `<div class="project-visual visual-${project.visual}" aria-hidden="true"><span>${content}</span><small>${project.mark}</small></div>`;
}
const links = (p) =>
  `<div class="project-links"><a class="project-demo" href="https://mateotrucco.github.io/${p.slug}/">${language === "es" ? "Abrir experiencia" : "Open experience"} <span>↗</span></a><a href="https://github.com/MateoTrucco/${p.slug}">${language === "es" ? "Código" : "Source"}</a></div>`;
function card(p, large = false) {
  return `<article class="${large ? "case-card" : "project-card"}" data-category="${p.category}" data-featured="${p.featured}" data-search="${[p.title, text(p.description), text(p.label), ...p.tech].join(" ").toLowerCase()}">${visual(p)}<div class="${large ? "case-body" : "project-body"}"><div class="project-meta"><span>${text(p.label)}</span><span>${p.tech.join(" · ")}</span></div><h3>${p.title}</h3><p>${text(p.description)}</p><div class="proof"><span>${language === "es" ? "Qué demuestra" : "What it demonstrates"}</span><strong>${text(p.proof)}</strong></div>${links(p)}</div></article>`;
}
function renderProjects() {
  $("#featuredProjects").innerHTML = PROJECTS.filter((p) => p.featured)
    .map((p) => card(p, true))
    .join("");
  $("#projectGrid").innerHTML = PROJECTS.map((p) => card(p)).join("");
  filterProjects();
}
function filterProjects() {
  const query = $("#projectSearch").value.trim().toLowerCase();
  let visible = 0;
  for (const card of $("#projectGrid").children) {
    const match =
        activeFilter === "all" ||
        card.dataset.category === activeFilter ||
        (activeFilter === "featured" && card.dataset.featured === "true"),
      search = !query || card.dataset.search.includes(query);
    card.hidden = !(match && search);
    if (!card.hidden) visible++;
  }
  $("#projectCount").textContent =
    language === "es"
      ? `${visible} proyecto${visible === 1 ? "" : "s"}`
      : `${visible} project${visible === 1 ? "" : "s"}`;
  $("#emptyState").hidden = visible !== 0;
}
function renderTerminal() {
  const lines = terminal[language][terminalIndex % terminal[language].length];
  $("#signalCode").innerHTML = lines
    .map(
      (line, i) =>
        `<div><span class="${i ? "check" : "prompt"}">${i ? "" : "$ "}</span>${line.replace(/^\$ /, "")}</div>`,
    )
    .join("");
}
function applyPreferences() {
  const theme = localStorage.getItem(THEME) || "light";
  root.dataset.theme = theme;
  root.lang = language;
  document.querySelector("meta[name=theme-color]").content =
    theme === "dark" ? "#090e18" : "#f2f5f8";
  document
    .querySelectorAll("[data-en][data-es]")
    .forEach((el) => (el.textContent = el.dataset[language]));
  document
    .querySelectorAll("[data-placeholder-en]")
    .forEach(
      (el) =>
        (el.placeholder =
          el.dataset[`placeholder${language === "es" ? "Es" : "En"}`]),
    );
  $(".language-toggle").textContent = language === "es" ? "EN" : "ES";
  $(".theme-toggle").textContent = theme === "dark" ? "☀" : "◐";
  $("#rotatingWord").textContent =
    words[language][wordIndex % words[language].length];
  renderTerminal();
  renderProjects();
  renderSkills();
}
function renderSkills() {
  const skills = [
    ["Backend & data", 7],
    ["Algorithms & models", 6],
    ["Interface systems", 9],
    ["Testing & validation", 9],
    ["Platform tooling", 4],
  ];
  $("#skillChart").innerHTML = skills
    .map(
      ([name, count]) =>
        `<div class="skill-row"><div><span>${language === "es" ? { "Backend & data": "Backend y datos", "Algorithms & models": "Algoritmos y modelos", "Interface systems": "Sistemas de interfaz", "Testing & validation": "Pruebas y validación", "Platform tooling": "Herramientas de plataforma" }[name] : name}</span><b>${count}/9</b></div><i><span style="width:${(count / 9) * 100}%"></span></i></div>`,
    )
    .join("");
}
function countUp() {
  document.querySelectorAll("[data-count]").forEach((el) => {
    const end = Number(el.dataset.count),
      start = performance.now(),
      duration = 850;
    const tick = (now) => {
      const progress = Math.min(1, (now - start) / duration);
      el.textContent = `${Math.round(end * (1 - (1 - progress) ** 3))}${el.dataset.suffix || ""}`;
      if (progress < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });
}
$(".theme-toggle").addEventListener("click", () => {
  localStorage.setItem(THEME, root.dataset.theme === "dark" ? "light" : "dark");
  applyPreferences();
});
$(".language-toggle").addEventListener("click", () => {
  language = language === "es" ? "en" : "es";
  localStorage.setItem(LANG, language);
  applyPreferences();
});
$("#rerunTerminal").addEventListener("click", () => {
  terminalIndex++;
  renderTerminal();
});
setInterval(() => {
  wordIndex++;
  const el = $("#rotatingWord");
  el.classList.add("swap");
  setTimeout(() => {
    el.textContent = words[language][wordIndex % words[language].length];
    el.classList.remove("swap");
  }, 180);
}, 4300);
document.querySelectorAll("[data-filter]").forEach((button) =>
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter;
    document.querySelectorAll("[data-filter]").forEach((item) => {
      const active = item === button;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-pressed", String(active));
    });
    filterProjects();
  }),
);
$("#projectSearch").addEventListener("input", filterProjects);
addEventListener("pointermove", (event) => {
  root.style.setProperty("--cursor-x", `${event.clientX}px`);
  root.style.setProperty("--cursor-y", `${event.clientY}px`);
});
const observer = new IntersectionObserver(
  (entries) =>
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    }),
  { threshold: 0.08 },
);
document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
$("#year").textContent = new Date().getFullYear();
applyPreferences();
countUp();
