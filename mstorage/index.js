const grid = document.getElementById("filmGrid");
const searchInput = document.getElementById("searchInput");

function renderCards(list) {
    grid.innerHTML = list.map(f => `
    <div class="card">
      <div class="cover">
        <img src="${f.cover}" alt="${escapeHtml(f.title)}">
      </div>
      <div class="overlay">
        ${escapeHtml(f.title)} <span class="year">(${f.year})</span>
      </div>
    </div>
  `).join('');
}

function escapeHtml(str) {
    return String(str).replace(/[&<>"]+/g, s => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'
    }[s]));
}

searchInput.addEventListener("input", () => {
    const q = searchInput.value.toLowerCase();
    const filtered = films.filter(f => f.title.toLowerCase().includes(q) || String(f.year).includes(q));
    renderCards(filtered);
});

renderCards(films);