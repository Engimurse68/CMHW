#region imports
from math import sqrt, pi, exp
from NumericalMethods import GPDF, Simpson, Probability
#endregion

#region function definitions
def main():

    #region testing user input
    # The following code solicites user input through the CLI.
    mean = input("Population mean? ")
    stDev = input("Standard deviation?")
    c = input("c value?")
    GT = True if input("Probability greater than c?").lower() in ["y","yes","true"] else "False"
    print("P(x"+(">" if GT else "<") + c +"|"+mean+", "+stDev +")")
    # First required probability: P(x < 105 | μ=100, σ=12.5)
    p_less_105 = Probability(GPDF, (100, 12.5), 105, GT=False)

    # Second required probability: P(x > μ + 2σ | μ=100, σ=3)
    # μ + 2σ = 100 + 6 = 106
    p_greater_106 = Probability(GPDF, (100, 3), 106, GT=True)

    # Print in the exact requested format (with two decimal places)
    print(f"P(x<105.00|N(100,12.5))={p_less_105:.2f}")
    print(f"P(x>106.00|N(100,3))={p_greater_106:.2f}")
    #endregion
#endregion

if __name__ == "__main__":
    main()