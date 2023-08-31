import splinepy as sp
import gustaf as gus


geometry = sp.BSpline(
    degrees=[1, 1],
    control_points=[
        [0.0, 0.0],
        [1.0, 0.0],
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

