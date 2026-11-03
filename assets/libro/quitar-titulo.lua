-- Quarto abre el libro con un `\chapter*` del título (la primera cabecera de index.qmd) que
-- queda como página 1, antes de la portada. La portada es la página 1: este filtro, que corre
-- tras los de Quarto, quita esa cabecera; el título sigue impreso en la portada y la portadilla.

local quitada = false

function Header(el)
  if quitada or not quarto.doc.is_format("pdf") then
    return nil
  end
  if el.level == 1 and el.classes:includes("unlisted") then
    quitada = true
    return {}
  end
  return nil
end
