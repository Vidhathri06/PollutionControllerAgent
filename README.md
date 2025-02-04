 ***Pollution Control Agent***

**Overview**

This project implements a utility-based agent designed to select the most effective pollution control strategy based on given preferences. The agent evaluates multiple strategies and selects the one that maximizes utility.

**Features**

-> Considers different pollution control strategies with attributes: pollution reduction, cost, and public acceptance.

-> Uses a weighted utility function to evaluate each strategy.

-> Selects the best strategy based on user-defined preferences.

**How It Works**

**1.** The agent stores predefined pollution control strategies with their attributes.

**2.** The user provides preferences for three factors:

**.** Pollution Reduction

**.** Cost

**.** Public Acceptance

**3.** The agent calculates the utility of each strategy using the formula:

**utility** = (pollution_reduction_weight * pollution_reduction) -
          (cost_weight * cost) +
          (public_acceptance_weight * public_acceptance)

**4.** The strategy with the highest utility is selected as the best option.
