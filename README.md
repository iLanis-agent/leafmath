# Leaf math

Leaf cleanup arithmetic: the lawn names the liters, the liters name the trips, and the pile names the bags.

Live at https://ilanis-agent.github.io/leafmath/

## The three tools

- **Pile plan** - liters = lawn area x leaf depth x 10, with rake-and-bag, tarp-hauling and blower-and-trailer bands.
- **Trip plan** - trips = ceil(liters / labeled 200 L tarp load), with couple-of-trips, shuttle-service and convoy bands.
- **Bag plan** - bags = ceil(liters / labeled 120 L bag), with curbside-armful, curbside-wall and city-vacuum bands.

## Formulas and limits

- Liters are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: liters per m2 per cm, tarp load, bag size.
- Illustrative planning arithmetic only. Wet leaves weigh and pack far more than dry ones, loose piles compress to a fraction in the bag, and raking is real work in bursts - pace it, and rake with the wind, not against it. This is not a landscaper's quote.

## Development

- `engine.js` - calculation and render engine (browser global `LeafMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
