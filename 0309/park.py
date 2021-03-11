import numpy as np
import numpy_financial as npf

cf = [-750, -250, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

cashflow = np.array(cf)
print(npf.irr(cashflow))
print(npf.npv(0.045, cashflow))
#174억으로 6.4%의 수익이 난다....