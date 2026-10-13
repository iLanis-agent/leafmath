import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

TARP_L = 200
BAG_L = 120

def leaf_liters(areaM2, depthCm):
    return round1(areaM2 * depthCm * 10)

def pile_plan(areaM2, depthCm):
    if not (areaM2 > 0) or not (depthCm > 0):
        return {"error": "the area and the depth must be positive"}
    liters = leaf_liters(areaM2, depthCm)
    if liters <= 500: verdict = "a rake-and-bag morning"
    elif liters <= 2000: verdict = "a tarp-hauling day"
    else: verdict = "a blower-and-trailer weekend"
    return {"liters": liters, "verdict": verdict}

def tarp_plan(areaM2, depthCm):
    if not (areaM2 > 0) or not (depthCm > 0):
        return {"error": "the area and the depth must be positive"}
    liters = leaf_liters(areaM2, depthCm)
    loads = math.ceil(liters / TARP_L)
    if loads <= 2: verdict = "a couple of trips"
    elif loads <= 6: verdict = "a shuttle service"
    else: verdict = "a convoy"
    return {"liters": liters, "loads": loads, "verdict": verdict}

def bag_plan(areaM2, depthCm):
    if not (areaM2 > 0) or not (depthCm > 0):
        return {"error": "the area and the depth must be positive"}
    liters = leaf_liters(areaM2, depthCm)
    bags = math.ceil(liters / BAG_L)
    if bags <= 5: verdict = "a curbside armful"
    elif bags <= 15: verdict = "a curbside wall"
    else: verdict = "a call for the city vacuum"
    return {"liters": liters, "bags": bags, "verdict": verdict}

def render_pile(r, areaM2, depthCm):
    return ("Your " + fmt(areaM2) + " m2 lawn under " + fmt(depthCm) + " cm of leaves holds " + fmt(r["liters"])
            + " L of leaves - " + r["verdict"] + ".")

def render_tarp(r, *args):
    return ("That " + fmt(r["liters"]) + " L pile at a labeled " + fmt(TARP_L) + " L a trip is "
            + plural(r["loads"], "trip") + " with the tarp - " + r["verdict"] + ".")

def render_bag(r, *args):
    return ("That " + fmt(r["liters"]) + " L pile at a labeled " + fmt(BAG_L) + " L a bag fills "
            + plural(r["bags"], "bag") + " - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[50,2],[20,1],[100,5],[40,3],[10,2],[60,4],[30,1],[80,3],[0,2],[50,0]]:
    add("pilePlan", pile_plan, render_pile, a)
for a in [[50,2],[20,1],[100,5],[10,2],[40,3],[80,3],[30,1],[60,2],[0,2],[60,0]]:
    add("tarpPlan", tarp_plan, render_tarp, a)
for a in [[50,2],[20,1],[100,5],[10,2],[40,3],[80,3],[30,1],[60,2],[0,1],[50,0]]:
    add("bagPlan", bag_plan, render_bag, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
