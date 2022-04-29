translucent = False
transparent = 1
is_cube = False
glass = False

colliders = [
	[
		(-0.4375, -0.5, -0.4375),
		( 0.4375,  0.5,  0.4375)
	]
]

vertex_positions = [
	[ 0.4375,  0.5000,  0.5000,  0.4375, -0.5000,  0.5000,  0.4375, -0.5000, -0.5000,  0.4375,  0.5000, -0.5000], # right
	[-0.4375,  0.5000, -0.5000, -0.4375, -0.5000, -0.5000, -0.4375, -0.5000,  0.5000, -0.4375,  0.5000,  0.5000], # left
	[ 0.5000,  0.5000,  0.5000,  0.5000,  0.5000, -0.5000, -0.5000,  0.5000, -0.5000, -0.5000,  0.5000,  0.5000], # top
	[-0.5000, -0.5000,  0.5000, -0.5000, -0.5000, -0.5000,  0.5000, -0.5000, -0.5000,  0.5000, -0.5000,  0.5000], # bottom
	[-0.5000,  0.5000,  0.4375, -0.5000, -0.5000,  0.4375,  0.5000, -0.5000,  0.4375,  0.5000,  0.5000,  0.4375], # front
	[ 0.5000,  0.5000, -0.4375,  0.5000, -0.5000, -0.4375, -0.5000, -0.5000, -0.4375, -0.5000,  0.5000, -0.4375], # back
]

tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]