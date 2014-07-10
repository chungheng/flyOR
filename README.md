# Fly Odor-Receptor Mapping #

This software serves to provide a macro-scale programming model for modeling the
odorant-receptor binding phenomena of the odor receptor population of the fruit
fly. Unlike the point transduction process which focuses on the dynamics of a
single receptor in response to odor stimulus, the approach employed here aims
to represent the response __pattern__ across all receptor types. In more details:

* For a given pair of odorant identity and concentration `(odor, c)`, the program
  returns a odor-response __pattern__. A pattern is a 50-dimensional vector, and each
  entry of pattern indicates the response of a unique receptor to the odorant `odor`
  under concentration `c`.
* For a fixed odorant, the pattern should vary under different concentration.
* The outcome of this program should will be used as the input to the transduction
  model of odor receptor, or to the functional model of the olfactory sensory neuron.
