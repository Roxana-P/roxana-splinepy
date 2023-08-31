import splinepy as sp
<<<<<<< HEAD
import gustaf as gus

=======

try:
    import gustaf as gus

    has_gus = True
except ImportError:
    has_gus = False
>>>>>>> 373632a4fc93fc84af535246b408d78bd43a9444

geometry = sp.BSpline(
    degrees=[1, 1],
    control_points=[
        [0.0, 0.0],
        [1.0, 0.0],
<<<<<<< HEAD
        [0.0, 5.0],
        [1.0, 5.0],
    ],
    knot_vectors=[[0, 0, 1, 1], [0, 0, 1, 1]],
)
geometry.elevate_degrees(0)
geometry.elevate_degrees(1)

geometry.insert_knots(0, 0.3)


# geometry = sp.io.json.load("cross.json")[0]
geometry.show()

initgeom = geometry.copy()

second = geometry.copy()
# second.refine_elements_by_aspect_ratio(2, [0])

third = geometry.copy()
third.refine_elements_by_aspect_ratio(2, [1])

# initgeom.jacobian([0, 0])

gus.show(initgeom, second, third)

=======
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
>>>>>>> 373632a4fc93fc84af535246b408d78bd43a9444
