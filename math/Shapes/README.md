# Shaping 
### Two primary edge function shaping methods 

- **Point-blended spline**
	- Manually configured
- **Polynomial curve**
	- True blending and biasing

## GeoGebra 

For now you can test out the curves in [GeoGebra](https://www.geogebra.org/calculator) 

### Setup Variables 

__Set up these variable sliders for BOTH options:__ 

>a=0.5			&emsp; _(Min=-1, Max=1, Steps~0.01)_ 								\
>b=0.7			&emsp; _(Min=-1, Max=1, Steps~0.01)_ 								\
>c=0.5			&emsp; _(Min=-1, Max=1, Steps~0.01)_ 								\
>d=-0.2			&emsp; _(Min=-1, Max=1, Steps~0.01)_ 								\
>g=-0.3			&emsp; _(Min=-1, Max=1, Steps~0.01)_ 
>
>l=-1			&emsp; _(Min=-1, Max=-0.6, Steps~0.025)_ 							\
>r=1				&emsp; _(Min=0.6, Max=1, Steps~0.025)_ 
>
>A=(l, a) 																	\
>B=(-0.5, b)										 							\
>C=(0, c) 																	\
>D=(0.5, d) 																	\
>G=(r, g) 
 
### To create the spline curve:  
|e=Spline({A,B,C,D,G},3) 

>>The spline is a simple direct curve. It can work well, but if we need dampening or suppression, we need to use the polynomial.
 
### To create the polynomial curve: 
*Add these two variables to the initial setup:* 									 	\
>s=0  			&emsp; _(Min=-1, Max=1, Steps~0.025)_ 						\
>>Adds biase; shifts curve up/down											

>k=0  			&emsp; _(Min=0, Max=1, Steps~0.01)_  						\
>>Blends curve; acts as a curve suppressor	

Create a line through the two endpoints (from A to G): 						\
>L(x) = a + ((g - a)/(r - l)) * (x - l)		&emsp; _(disable visualization)_ 
 
Create the polynomial: 														\
>P(x)=Polynomial({A,B,C,D,G}) 				&emsp; _(disable visualization)_ 
 
Then create our belended function: 											\
>M(x) = (1 - k) * P(x) + k * L(x) +s   										\
 
_This is the primary curve, we adjust `s` to raise/lower bias and `k` to saturate/blend the curve to the endpoint line_ 
 
## Notes!
- Everything should be constrained in a [-1, 1] box
- For now, control ranges are manually constrained to preserve interpretability and reduce extreme overlap outside the normalized [-1,1] domain. Additional limiting functions or normalization methods might be introduced later if needed.
- At k = 0, the response is ___fully polynomial___ and preserves maximum nonlinear shaping. At k = 1, the response collapses fully to the ___endpoint line___. Intermediate values of k produce a weighted blend between the two. The offset term s shifts the resulting curve vertically without changing the blend relationship itself.
