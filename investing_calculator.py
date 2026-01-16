import numpy as np
import matplotlib.pyplot as plt

def project_portfolio(starting_pot, monthly_contrib, annual_return, years=30):
    """
    Projects portfolio value with monthly contributions and monthly compounding.
    """
    months = years * 12
    r = (1 + annual_return) ** (1/12) - 1  # annual -> monthly
    values = np.zeros(months + 1)
    values[0] = starting_pot

    for m in range(1, months + 1):
        values[m] = values[m - 1] * (1 + r) + monthly_contrib

    return values

def total_contributed(starting_pot, monthly_contrib, years=30):
    months = years * 12
    contrib = np.zeros(months + 1)
    for m in range(months + 1):
        contrib[m] = starting_pot + monthly_contrib * m
    return contrib

def main():
    # ---- User inputs ----
    starting_pot = float(input("Starting pot size (e.g., 10000): ").strip())
    monthly_contrib = float(input("Monthly contribution (e.g., 500): ").strip())

    years = 30
    months = years * 12
    t_years = np.arange(months + 1) / 12

    # ---- Market scenarios (annual returns) ----
    scenarios = {
        "Bad (3%/yr)": 0.03,
        "Average (7%/yr)": 0.07,
        "Good (10%/yr)": 0.10
    }

    # ---- Projections ----
    results = {}
    for name, r in scenarios.items():
        results[name] = project_portfolio(starting_pot, monthly_contrib, r, years)

    contrib_line = total_contributed(starting_pot, monthly_contrib, years)

    # ---- Plot ----
    plt.figure()
    for name, vals in results.items():
        plt.plot(t_years, vals, label=name)

    plt.plot(t_years, contrib_line, linestyle="--", label="Total Contributed")

    plt.title(f"Portfolio Growth vs Contributions ({years} years)")
    plt.xlabel("Years")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # ---- Summary output ----
    print(f"\nTotal contributed after {years} years: {contrib_line[-1]:,.2f}\n")
    print("Ending portfolio values:")
    for name, vals in results.items():
        gain = vals[-1] - contrib_line[-1]
        print(f"  {name}: {vals[-1]:,.2f}  (Gain: {gain:,.2f})")

if __name__ == "__main__":
    main()
