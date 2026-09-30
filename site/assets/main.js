document.documentElement.classList.add('js');
const menu = document.querySelector('.menu');
const links = document.querySelector('#navigation');
if (menu && links) {
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    menu.textContent = open ? 'Close' : 'Menu';
    links.classList.toggle('open', open);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      menu.setAttribute('aria-expanded', 'false');
      menu.textContent = 'Menu';
      links.classList.remove('open');
      menu.focus();
    }
  });
}
