import numpy as np
import scipy
from time import perf_counter


def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Function {func.__name__} completed in {(end - start)} seconds")
        return result
    return wrapper


@timer
def scipy_stats_multivariate_normal_logpdf(x: np.array, m: np.array, c: np.array) -> np.array:
    return scipy.stats.multivariate_normal(m, c).logpdf(x)


@timer
def logpdf_normal_multivariate(x: np.array, m: np.array, c: np.array) -> np.array:
    quad_form = np.sum((x - m) * np.dot(x - m, np.linalg.inv(c)), axis=1)
    logpdf = -0.5 * (np.log(2 * np.pi) + np.log(np.linalg.det(c)) + quad_form)
    return logpdf


if __name__ == '__main__':
    x = np.array([[2, 6], [1, 4]])
    m = np.array([0, 0])
    cov = np.array([[1, 0.5], [0.5, 2]])
    my_result = logpdf_normal_multivariate(x, m, cov)
    scipy_result = scipy_stats_multivariate_normal_logpdf(x, m, cov)
    print("Result:", my_result)
    print("Result:", scipy_result)
    difference = np.array(abs(scipy_result-my_result))
    print("Difference in results on average is:", sum(difference)/len(difference))
