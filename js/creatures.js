String.prototype.format = function () {
  a = this;
  for (k in arguments) {
    a = a.replace("{" + k + "}", arguments[k]);
  }
  return a;
};

function addSpellLinks() {
  const spellUrl = "http://2e.aonprd.com/Spells.aspx?ID={0}";

  const spellElems = document.getElementsByTagName("spell");
  for (let i = 0; i < spellElems.length; i++) {
    const spellElem = spellElems[i];
    const id = spellElem.getAttribute("spellid");

    if (id !== null) {
      const a = document.createElement("a");
      a.href = spellUrl.format(id);
      a.textContent = spellElem.textContent;
      spellElem.textContent = null;
      spellElem.appendChild(a);
    }
  }
}

document.addEventListener("DOMContentLoaded", addSpellLinks);
