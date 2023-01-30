# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

import numpy
import statistics


def _z(x: numpy.float64,
       mean: numpy.float64,
       standard_deviation: numpy.float64) -> numpy.float64:
    '''Функция расчета отклонения Z.
    :param x: Значение.
    :param mean: Среднее значение.
    :param standard_deviation: Среднее квадратичное отклонение.
    :return: Отклонение Z.
    '''
    return (x-mean)/standard_deviation


if __name__ == '__main__':

    mean = numpy.float64(174.0)
    standard_deviation = numpy.float64(8.0)
    nd = statistics.NormalDist(mean, standard_deviation)

    print('Средний рост населения города X имеющего нормальное распределение',
          'равен 174 см, а среднее квадратичное отклонение равно 8 см')

    x_150 = numpy.float64(150.0)
    x_158 = numpy.float64(158.0)
    x_166 = numpy.float64(166.0)
    x_182 = numpy.float64(182.0)
    x_190 = numpy.float64(190.0)
    x_198 = numpy.float64(198.0)

    print('Вероятность, что рост больше 182 см:',
          1 - nd.cdf(x_182))

    print('Вероятность, что рост больше 190 см:',
          1 - nd.cdf(x_190))

    print('Вероятность, что рост от 166 см до 190 см:',
          nd.cdf(x_190) - nd.cdf(x_166))

    print('Вероятность, что рост от 166 см до 182 см:',
          nd.cdf(x_182) - nd.cdf(x_166))

    print('Вероятность, что рост от 158 см до 190 см:',
          nd.cdf(x_190) - nd.cdf(x_158))

    print('Вероятность, что рост не выше 150 см или не ниже 190 см:',
          nd.cdf(x_150) + (1 - nd.cdf(x_190)))

    print('Вероятность, что рост не выше 150 см или не ниже 198 см:',
          nd.cdf(x_150) + (1 - nd.cdf(x_198)))

    print('Вероятность, что рост ниже 166 см:',
          nd.cdf(x_166))