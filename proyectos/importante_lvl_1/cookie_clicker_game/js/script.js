let cookies = getCookie("cookies") || 0;
let cookiesPerClick = getCookie("cookiesPerClick") || 1;
let cookiesPerSecond = getCookie("cookiesPerSecond") || 0;
let upgradeCost = getCookie("upgradeCost") || 10;
let cursorCost = getCookie("cursorCost") || 100;
let cursors = getCookie("cursors") || 0;
let grandmas = getCookie("grandmas") || 0;

function clickCookie() {
  cookies += cookiesPerClick;
  updateCookieCount();
  saveDataToCookies();
}

function buyUpgrade() {
  if (cookies >= upgradeCost) {
    cookies -= upgradeCost;
    cookiesPerClick += 1;
    upgradeCost *= 1.5;
    updateCookieCount();
    updateCookiesPerClick();
    updateUpgradeCost();
    saveDataToCookies();
  } else {
    alert("No tienes suficientes cookies para comprar la mejora.");
  }
}

function buyCursor() {
  if (cookies >= cursorCost) {
    cookies -= cursorCost;
    cursors += 1;
    cursorCost *= 1.5;
    updateCookieCount();
    updateCursors();
    updateCursorCost();
    saveDataToCookies();
  } else {
    alert("No tienes suficientes cookies para comprar el cursor.");
  }
}

function buyGrandma() {
  cookies += cookiesPerClick;
  updateGrandmaCount();
  saveDataToCookies();
}

function updateCookieCount() {
  document.getElementById("cookies").innerText = "Cookies: " + cookies;
}

function updateGrandmaCount() {
  document.getElementById("grandmas").innerText = "ABUELASSSS: " + grandmas;
}

function updateCookiesPerClick() {
  document.getElementById("cookies-per-click").innerText =
    "Cookies por clic: " + cookiesPerClick;
}

function updateCookiesPerSecond() {
  document.getElementById("cookies-per-second").innerText =
    "Cookies por segundo: " + cookiesPerSecond;
}

function updateUpgradeCost() {
  document.querySelector(
    "#upgrade-container .upgrade-button"
  ).innerText = `Mejora (Costo: ${upgradeCost} cookies)`;
}

function updateCursorCost() {
  document.querySelectorAll(
    "#upgrade-container .upgrade-button"
  )[1].innerText = `Comprar Cursor (Costo: ${cursorCost} cookies)`;
}

function updateCursors() {
  const cursorsContainer = document.getElementById("cursors-container");
  cursorsContainer.innerHTML = "";

  for (let i = 0; i < cursors; i++) {
    const cursorElement = document.createElement("div");
    cursorElement.classList.add("cursor");
    cursorsContainer.appendChild(cursorElement);
  }
}

function autoClicker() {
  cookiesPerSecond = cursors;
  cookies += cookiesPerSecond;
  updateCookieCount();
  updateCookiesPerSecond();
  saveDataToCookies();
}

function saveDataToCookies() {
  setCookie("cookies", cookies);
  setCookie("cookiesPerClick", cookiesPerClick);
  setCookie("cookiesPerSecond", cookiesPerSecond);
  setCookie("upgradeCost", upgradeCost);
  setCookie("cursorCost", cursorCost);
  setCookie("cursors", cursors);
    a = 2
}

function setCookie(name, value) {
  document.cookie = `${name}=${value}; expires=Thu, 18 Dec 2030 12:00:00 UTC; path=/`;
}

function getCookie(name) {
  const cookies = document.cookie.split(";");
  for (let cookie of cookies) {
    const [cookieName, cookieValue] = cookie.split("=");
    if (cookieName.trim() === name) {
      return parseFloat(cookieValue); // Cambiamos a parseFloat para asegurarnos de obtener un número
    }
  }
  return null;
}

setInterval(autoClicker, 1000);

// Inicialización
updateCookieCount();
updateCookiesPerClick();
updateCookiesPerSecond();
updateUpgradeCost();
updateCursorCost();
updateCursors();
