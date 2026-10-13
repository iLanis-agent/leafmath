(function (root) {
  "use strict";
  var TARP_L = 200; // labeled tarp load, liters
  var BAG_L = 120;  // labeled paper leaf bag, liters

  function round1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function leafLiters(areaM2, depthCm) {
    return round1(areaM2 * depthCm * 10);
  }

  function pilePlan(areaM2, depthCm) {
    if (!(areaM2 > 0) || !(depthCm > 0)) return { error: "the area and the depth must be positive" };
    var liters = leafLiters(areaM2, depthCm);
    var verdict;
    if (liters <= 500) verdict = "a rake-and-bag morning";
    else if (liters <= 2000) verdict = "a tarp-hauling day";
    else verdict = "a blower-and-trailer weekend";
    return { liters: liters, verdict: verdict };
  }

  function tarpPlan(areaM2, depthCm) {
    if (!(areaM2 > 0) || !(depthCm > 0)) return { error: "the area and the depth must be positive" };
    var liters = leafLiters(areaM2, depthCm);
    var loads = Math.ceil(liters / TARP_L);
    var verdict;
    if (loads <= 2) verdict = "a couple of trips";
    else if (loads <= 6) verdict = "a shuttle service";
    else verdict = "a convoy";
    return { liters: liters, loads: loads, verdict: verdict };
  }

  function bagPlan(areaM2, depthCm) {
    if (!(areaM2 > 0) || !(depthCm > 0)) return { error: "the area and the depth must be positive" };
    var liters = leafLiters(areaM2, depthCm);
    var bags = Math.ceil(liters / BAG_L);
    var verdict;
    if (bags <= 5) verdict = "a curbside armful";
    else if (bags <= 15) verdict = "a curbside wall";
    else verdict = "a call for the city vacuum";
    return { liters: liters, bags: bags, verdict: verdict };
  }

  function renderPile(r, areaM2, depthCm) {
    return "Your " + areaM2 + " m2 lawn under " + depthCm + " cm of leaves holds " + r.liters
      + " L of leaves - " + r.verdict + ".";
  }

  function renderTarp(r) {
    return "That " + r.liters + " L pile at a labeled " + TARP_L + " L a trip is "
      + plural(r.loads, "trip") + " with the tarp - " + r.verdict + ".";
  }

  function renderBag(r) {
    return "That " + r.liters + " L pile at a labeled " + BAG_L + " L a bag fills "
      + plural(r.bags, "bag") + " - " + r.verdict + ".";
  }

  var api = { pilePlan: pilePlan, tarpPlan: tarpPlan, bagPlan: bagPlan, renderPile: renderPile, renderTarp: renderTarp, renderBag: renderBag };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.LeafMath = api;
})(this);
