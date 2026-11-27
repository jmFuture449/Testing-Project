def compound_interest(p: float, r: float, n: int, t: int) -> float:
    """
    Return the accumulated amount, compounded n times per year for t years.

    p is the principal, r is the annual rate (e.g., 0.05), n is the number
    of compounding periods per year, and t is the number of years.
    """
    return p * (1 + r / n) ** (n * t)