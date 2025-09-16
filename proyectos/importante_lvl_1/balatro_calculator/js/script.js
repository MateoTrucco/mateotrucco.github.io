const valoresValidos = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
const palosValidos = ['♠', '♣', '♥', '♦'];

// Valores base de manos (chips, mult) por nivel 1
const manosBase = {
  high_card: { chips: 5, mult: 1 },
  pair: { chips: 10, mult: 2 },
  two_pair: { chips: 20, mult: 2 },
  three_of_a_kind: { chips: 30, mult: 3 },
  straight: { chips: 35, mult: 4 },
  flush: { chips: 35, mult: 4 },
  full_house: { chips: 40, mult: 4 },
  four_of_a_kind: { chips: 60, mult: 7 },
  straight_flush: { chips: 100, mult: 8 },
  five_of_a_kind: { chips: 120, mult: 12 },
  flush_house: { chips: 140, mult: 14 },
  flush_five: { chips: 150, mult: 16 }
};

// Efectos de modificadores
const mejorasEfectos = {
  glass: { mult: 2, chips: 0 },
  steel: { mult: 1.5, chips: 0 },
  gold: { chips: 50, mult: 0 },
  lucky: { mult: 1.2, chips: 20 }
};

const edicionesEfectos = {
  foil: { chips: 50, mult: 0 },
  holo: { chips: 0, mult: 10 },
  poly: { chips: 50, mult: 4 },
  base: { chips: 0, mult: 0 }
};

const sellosEfectos = {
  rojo: { mult: 1, chips: 10 },
  dorado: { chips: 30, mult: 0 },
  azul: { chips: 20, mult: 0 },
  purpura: { mult: 1.5, chips: 0 },
  none: { chips: 0, mult: 0 }
};

// Variables globales
let cartas = Array(8).fill().map(() => ({ valor: '2', palo: '♠', mejora: null, edicion: 'base', sello: 'none' }));
let cartaSeleccionada = 0;

// Configuración para el efecto 3D
const constrain = 5; // Controla la intensidad de la rotación
const perspective = 94; // Perspectiva para el efecto 3D

// Calcular transformación 3D basada en la posición del mouse
function transforms(x, y, el) {
  const box = el.getBoundingClientRect();
  const calcX = -(y - box.y - (box.height / 2)) / (el.dataset.scale == 2 ? constrain * 2 : constrain);
  const calcY = (x - box.x - (box.width / 2)) / (el.dataset.scale == 2 ? constrain * 2 : constrain);

  return `perspective(${perspective}px) rotateX(${calcX}deg) rotateY(${calcY}deg)`;
}

// Manejar evento mouseover
function hoverCard(e) {
  const target = e.target.closest('button[data-carta]');
  if (target) {
    target.style.transform = transforms(e.clientX, e.clientY, target);
  }
}

// Manejar evento mouseout
function noHoverCard(e) {
  const target = e.target.closest('button[data-carta]');
  if (target) {
    target.style.transform = '';
  }
}

// Seleccionar carta
function seleccionarCarta(index) {
  cartaSeleccionada = index;
  document.querySelectorAll('[data-carta]').forEach((btn, i) => {
    btn.classList.toggle('selected', i === index);
  });
  cargarModificadores();
}

// Aplicar cambios a la carta actual
function aplicarCambios() {
  const valorInput = document.querySelector('input[name="valor"]').value.toUpperCase();
  const palo = document.querySelector('select[name="palo"]').value;
  const mejora = document.querySelector('input[name="mejora"]:checked')?.value || null;
  const edicion = document.querySelector('select[name="edicion"]').value;
  const sello = document.querySelector('select[name="sello"]').value;

  if (valoresValidos.includes(valorInput) && palosValidos.includes(palo)) {
    cartas[cartaSeleccionada] = { valor: valorInput, palo, mejora, edicion, sello };
    actualizarVisualCarta(cartaSeleccionada);
  } else {
    alert('Por favor, ingresa un valor válido (2-10, J, Q, K, A) y un palo válido.');
  }
}

// Actualizar texto de la carta
function actualizarVisualCarta(index) {
  const btn = document.querySelector(`[data-carta="${index}"]`);
  const { valor, palo, mejora, edicion, sello } = cartas[index];
  btn.innerHTML = `${valor}<span>${palo}${mejora ? ' ' + mejora : ''}${edicion !== 'base' ? ' ' + edicion : ''}${sello !== 'none' ? ' ' + sello : ''}</span>`;
}

// Cargar modificadores a los controles para la carta seleccionada
function cargarModificadores() {
  const carta = cartas[cartaSeleccionada];
  document.querySelector('input[name="valor"]').value = carta.valor;
  document.querySelector('select[name="palo"]').value = carta.palo;
  document.querySelectorAll('input[name="mejora"]').forEach(r => r.checked = r.value === carta.mejora);
  document.querySelector('select[name="edicion"]').value = carta.edicion;
  document.querySelector('select[name="sello"]').value = carta.sello;
}

// Calcular puntuación de una mano
function calcularPuntuacion() {
  const mano = document.querySelector('#mano').value;
  const nivel = parseInt(document.querySelector('#nivelManoInput').value) || 1;
  const modoOptimo = document.querySelector('#modoOptimo').checked;
  const resultadoDiv = document.querySelector('#resultado');
  const cargandoDiv = document.querySelector('#cargando');

  if (modoOptimo) {
    cargandoDiv.style.display = 'block';
    setTimeout(() => {
      const mejorResultado = calcularMejorMano();
      cargandoDiv.style.display = 'none';
      resultadoDiv.textContent = `Mejor mano: ${mejorResultado.mano} (Nvl. ${mejorResultado.nivel})\nChips: ${mejorResultado.chips}\nMult: ${mejorResultado.mult}\nTotal: ${mejorResultado.total}\nCartas usadas: ${mejorResultado.cartas.map(c => `${c.valor}${c.palo}`).join(', ')}`;
    }, 100); // Simula carga
  } else {
    const { chips, mult } = calcularMano(mano, nivel);
    const total = chips * mult;
    resultadoDiv.textContent = `Mano: ${mano} (Nvl. ${nivel})\nChips: ${chips}\nMult: ${mult}\nTotal: ${total}`;
  }

  // Actualizar panel lateral
  document.querySelector('#puntajeActual').textContent = Math.round(chips * mult);
  document.querySelector('#nivelMano').textContent = `Nvl.${nivel}`;
  document.querySelector('#valorCartaAlta').textContent = manosBase[mano].chips;
}

// Calcular puntuación de una mano específica
function calcularMano(mano, nivel) {
  let chips = manosBase[mano].chips + (nivel - 1) * 10; // Incremento de chips por nivel
  let mult = manosBase[mano].mult + (nivel - 1); // Incremento de mult por nivel

  cartas.forEach(carta => {
    if (carta.mejora) {
      chips += mejorasEfectos[carta.mejora].chips;
      mult += mejorasEfectos[carta.mejora].mult;
    }
    if (carta.edicion !== 'base') {
      chips += edicionesEfectos[carta.edicion].chips;
      mult += edicionesEfectos[carta.edicion].mult;
    }
    if (carta.sello !== 'none') {
      chips += sellosEfectos[carta.sello].chips;
      mult += sellosEfectos[carta.sello].mult;
    }
  });

  return { chips: Math.round(chips), mult: Math.round(mult) };
}

// Calcular la mejor mano posible
function calcularMejorMano() {
  const niveles = Array.from({ length: 10 }, (_, i) => i + 1);
  const manos = Object.keys(manosBase);
  let mejorResultado = { mano: 'high_card', nivel: 1, chips: 0, mult: 0, total: 0, cartas: [] };

  for (const mano of manos) {
    for (const nivel of niveles) {
      const { chips, mult } = calcularMano(mano, nivel);
      const total = chips * mult;
      if (total > mejorResultado.total) {
        mejorResultado = { mano, nivel, chips, mult, total, cartas: [...cartas] };
      }
    }
  }

  return mejorResultado;
}

window.addEventListener('DOMContentLoaded', () => {
  // Inicializar cartas con valores predeterminados
  cartas = [
    { valor: 'Q', palo: '♠', mejora: null, edicion: 'base', sello: 'none' },
    { valor: '10', palo: '♠', mejora: null, edicion: 'base', sello: 'none' },
    { valor: '9', palo: '♠', mejora: null, edicion: 'base', sello: 'none' },
    { valor: '8', palo: '♣', mejora: null, edicion: 'base', sello: 'none' },
    { valor: '5', palo: '♠', mejora: null, edicion: 'base', sello: 'none' },
    { valor: '4', palo: '♠', mejora: null, edicion: 'base', sello: 'none' },
    { valor: '3', palo: '♠', mejora: null, edicion: 'base', sello: 'none' },
    { valor: '2', palo: '♣', mejora: null, edicion: 'base', sello: 'none' }
  ];
  cartas.forEach((_, index) => actualizarVisualCarta(index));

  // Agregar eventos de selección y transformación 3D
  // Removed unused variable declaration for 'cartasArea'
  document.querySelectorAll('[data-carta]').forEach((btn, index) => {
    btn.addEventListener('click', () => seleccionarCarta(index));
    btn.addEventListener('mousemove', hoverCard);
    btn.addEventListener('mouseout', noHoverCard);
  });

  // Agregar eventos para modificadores
  document.querySelector('input[name="valor"]').addEventListener('change', aplicarCambios);
  document.querySelector('select[name="palo"]').addEventListener('change', aplicarCambios);
  document.querySelectorAll('input[name="mejora"]').forEach(input => {
    input.addEventListener('change', aplicarCambios);
  });
  document.querySelector('select[name="edicion"]').addEventListener('change', aplicarCambios);
  document.querySelector('select[name="sello"]').addEventListener('change', aplicarCambios);
  document.querySelector('#calcular-btn').addEventListener('click', calcularPuntuacion);

  // Seleccionar la primera carta
  seleccionarCarta(0);
});