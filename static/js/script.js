(() => {
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  const storageKey = 'mateo-portfolio-theme';

  const readStoredTheme = () => {
    try { return localStorage.getItem(storageKey); } catch { return null; }
  };
  const writeStoredTheme = (theme) => {
    try { localStorage.setItem(storageKey, theme); } catch { /* Storage may be disabled. */ }
  };
  const storedTheme = readStoredTheme();
  const preferredTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  const initialTheme = storedTheme === 'light' || storedTheme === 'dark' ? storedTheme : preferredTheme;

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    toggle?.setAttribute('aria-pressed', String(theme === 'light'));
    toggle?.setAttribute('aria-label', `Switch to ${theme === 'light' ? 'dark' : 'light'} theme`);
  };
  applyTheme(initialTheme);

  toggle?.addEventListener('click', () => {
    const next = root.dataset.theme === 'light' ? 'dark' : 'light';
    applyTheme(next);
    writeStoredTheme(next);
  });

  const buttons = [...document.querySelectorAll('[data-filter]')];
  const cards = [...document.querySelectorAll('[data-categories]')];
  const emptyState = document.querySelector('.empty-state');

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter ?? 'all';
      let visible = 0;
      buttons.forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      cards.forEach((card) => {
        const categories = (card.dataset.categories ?? '').split(/\s+/);
        const show = filter === 'all' || categories.includes(filter);
        card.hidden = !show;
        if (show) visible += 1;
      });
      if (emptyState) emptyState.hidden = visible !== 0;
    });
  });

  const year = document.querySelector('#year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
