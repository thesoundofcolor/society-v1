# Shaping
### Two primary edge shaping methods

- **Point-blended spline**
	- Manually configured
- **Polynomial curve**
	- True blending and biasing

## GeoGebra

For now you can test out the curves in [GeoGebra](https://www.geogebra.org/calculator)

### Setup Variables

__Set up these variable sliders for BOTH options:__

a=0.5			_(Min=-1, Max=1, Steps~0.01)_
b=0.7			_(Min=-1, Max=1, Steps~0.01)_
c=0.5			_(Min=-1, Max=1, Steps~0.01)_
d=-0.2			_(Min=-1, Max=1, Steps~0.01)_
g=-0.3			_(Min=-1, Max=1, Steps~0.01)_

l=-1			_(Min=-1, Max=-0.6, Steps~0.025)_
r=1				_(Min=0.6, Max=1, Steps~0.025)_

A=(l, a)
B=(-0.5, b)
C=(0, c)
D=(0.5, d)
G=(r, g)

1) To get Spline: 
e=Spline({A,B,C,D,G},3)

2) To get Curve:

A couple more variables:
s=0  _(Min=-1, Max=1, Steps~0.025)_
k=0  _(Min=0, Max=1, Steps~0.01)_

Create a line through the two endpoints (A and G):
L(x) = a + ((g - a)/(r - l)) * (x - l)		_(disable visualization)_

Create the polynomial: 
P(x)=Polynomial({A,B,C,D,G}) 				_(disable visualization)_

Then create our belended function:
M(x) = (1 - k) * P(x) + k * L(x) +s    _(this is the primary curve, we adjust `s` to raise/lower bias and `k` to saturate/blend the curve to the endpoint line)_

## Notes!
- Everything should be constrained in a [-1, 1] box
- For now, control ranges are manually constrained to preserve interpretability and reduce extreme overlap outside the normalized [-1,1] domain. Additional limiting functions or normalization methods might be introduced later if needed.
- At k = 0, the response is ___fully polynomial___ and preserves maximum nonlinear shaping. At k = 1, the response collapses fully to the ___endpoint line___. Intermediate values of k produce a weighted blend between the two. The offset term s shifts the resulting curve vertically without changing the blend relationship itself.
