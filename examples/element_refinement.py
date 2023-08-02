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
        [0.0, 1.0],
        [1.0, 1.0],
    ],
    knot_vectors=[[0, 0, 1, 1], [0, 0, 1, 1]],
)

geometry = gus.spline.io.json.load("cross.json")[0]

initgeom = geometry.copy()
geometry.refine_elements_by_aspect_ratio(20, [1])
second = geometry.copy()
geometry.refine_elements_by_aspect_ratio(20, [1])
third = geometry.copy()

if has_gus:
    gus.show(
        gus.NURBS(**initgeom.todict()),
        gus.NURBS(**second.todict()),
        gus.NURBS(**third.todict()),
        gus.NURBS(**geometry.todict()),
    )
