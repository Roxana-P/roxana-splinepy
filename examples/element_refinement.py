import splinepy as sp

try:
    import gustaf as gus

    has_gus = True
except ImportError:
    has_gus = False

geometry = sp.BSpline(
    degrees=[1, 1],
    control_points=[
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 10.0],
        [1.0, 10.0],
    ],
    knot_vectors=[[0, 0, 1, 1], [0, 0, 1, 1]],
)
geometry.elevate_degree(0)
geometry.elevate_degree(1)

geometry.insert_knots(1, [1 / 10, 2 / 10, 3 / 10])

# Refine splines iteratively aspect ratio is reached
splines = [geometry.copy()]
refined = [True]
while any(refined):
    refined = geometry.refine_elements_by_aspect_ratio(2)
    splines.append(geometry.copy())


if has_gus:
    gus_splines = [gus.BSpline(**spline.todict()) for spline in splines]
    gus.show.show_vedo(*gus_splines)
