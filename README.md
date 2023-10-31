# ISDN2603 Tensile Test
Tensile test data parsing and analysis

## Usage

1. Manually install needed dependencies.
2. Update `reader.py` to confirm `cross_sectional_areas` well-defined. 
3. Run `reader.py` with .dat files in the directory.
4. Zoom in repetitively at required points, such as proof point, fracture point, if required.

Note that this is **alpha-quality** software and is not intended for non-developers to use it. 

Problems may be arise with other `.dat` files, and the user is expected to fix the bugs, change constants, or add new features on-the-fly. 

_Fortunately, with the given_ `.dat` _files, the graphs and correct values show up without user intervention._

## Example

<img width="483" alt="image" src="https://github.com/evnchn/ISDN2603-Tensile-Test/assets/37951241/a9e11e30-b16f-4371-a0ec-f62b207ed8e4">

By zooming in repetitively to find proof point:

<img width="483" alt="image" src="https://github.com/evnchn/ISDN2603-Tensile-Test/assets/37951241/c1a70c1f-a5e7-4601-9d09-c7926157f755">
