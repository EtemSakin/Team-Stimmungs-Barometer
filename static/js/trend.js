"use strict";
(function () {
  const dataTag = document.getElementById("trend-data");
  const canvas = document.getElementById("mood-trend-chart");
  if (!dataTag || !canvas) return;
  let points;
  try { points = JSON.parse(dataTag.textContent); }
  catch (error) { canvas.replaceChildren(); return; }
  const namespace = "http://www.w3.org/2000/svg";
  function node(tag, attrs, text) {
    const element = document.createElementNS(namespace, tag);
    Object.entries(attrs).forEach(([key, value]) => element.setAttribute(key, value));
    if (text !== undefined) element.textContent = text;
    return element;
  }
  const y = value => 240 - (value - 1) * 48;
  const x = index => 49 + index * 103;
  canvas.replaceChildren();
  for (let value = 1; value <= 5; value++) {
    canvas.appendChild(node("line", {x1:49,y1:y(value),x2:667,y2:y(value),class:"grid-line"}));
    canvas.appendChild(node("text", {x:27,y:y(value)+5,class:"axis-label","text-anchor":"middle"}, String(value)));
  }
  points.forEach((point, i) => canvas.appendChild(node("text", {x:x(i),y:265,class:"axis-label","text-anchor":"middle"}, point.label)));
  for (let i = 1; i < points.length; i++) {
    if (points[i - 1].average === null || points[i].average === null) continue;
    canvas.appendChild(node("line", {x1:x(i-1),y1:y(points[i-1].average),x2:x(i),y2:y(points[i].average),class:"trend-path"}));
  }
  let hasData = false;
  points.forEach((point, i) => {
    if (point.average === null) return;
    hasData = true;
    const circle = node("circle", {cx:x(i),cy:y(point.average),r:7,class:"trend-dot"});
    circle.appendChild(node("title", {}, point.label + ": " + point.average.toLocaleString("de-DE") + " von 5"));
    canvas.appendChild(circle);
  });
  if (!hasData) canvas.appendChild(node("text", {x:360,y:130,"text-anchor":"middle",fill:"#68766a","font-size":"17"}, "Noch keine freigegebenen Tageswerte"));
})();
