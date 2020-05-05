String.prototype.format = function () {
  a = this;
  for (k in arguments) {
    a = a.replace("{" + k + "}", arguments[k]);
  }
  return a;
};

function addSpellLinksTo(spellsElems) {
  const spellUrl = "http://2e.aonprd.com/Spells.aspx?ID={0}";

  for (let j = 0; j < spellsElems.length; j++) {
    spellsElem = spellsElems[j];

    const spellElems = spellsElem.getElementsByTagName("spell");
    for (let i = 0; i < spellElems.length; i++) {
      const spellElem = spellElems[i];
      const id = spellElem.getAttribute("spellid");

      if (id !== null) {
        const a = document.createElement("a");
        a.href = spellUrl.format(id);
        a.textContent = spellElem.textContent;
        spellElem.textContent = null;
        spellElem.appendChild(a);
        if (i == spellElems.length - 1) {
          a.textContent += ";";
        } else {
          a.textContent += ",";
        }
      } else {
        if (i == spellElems.length - 1) {
          spellElem.textContent += ";";
        } else {
          spellElem.textContent += ",";
        }
      }
    }
  }
}

function addSpellLinks() {
  const spellsElems = document.getElementsByTagName("spells");
  addSpellLinksTo(spellsElems);
  const cantripsElems = document.getElementsByTagName("cantrips");
  addSpellLinksTo(cantripsElems);
}

document.addEventListener("DOMContentLoaded", addSpellLinks);
