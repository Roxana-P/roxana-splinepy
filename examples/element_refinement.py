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


initgeom = geometry.copy()
geometry.refine_elements_by_aspect_ratio(2)
second = geometry.copy()
geometry.refine_elements_by_aspect_ratio(2)
third = geometry.copy()


gus.show(
    gus.BSpline(**initgeom.todict()),
    gus.BSpline(**second.todict()),
    gus.BSpline(**third.todict()),
    gus.BSpline(**geometry.todict()),
)

if has_gus:
    gus_splines = [gus.BSpline(**spline.todict()) for spline in splines]
    gus.show.show_vedo(*gus_splines)
