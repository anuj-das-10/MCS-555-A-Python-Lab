def get_gross_salary(basic):
    da = 0.4 * basic
    hra = 0.15 * basic
    return basic + da + hra


def get_net_salary(basic):
  pf = 0.12 * basic
  itax = 0.1 * basic
  return get_gross_salary(basic) - pf - itax