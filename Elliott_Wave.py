from matplotlib import pyplot as plt
from engine.iexfinance import *

def bearsishtrend():
    timeperiodwave1 = startwave1 - endwave1

    # Calculate the second wave

    candlewave2 = goldenratio[1] * candlewave1
    startwave2 = endwave1
    timeperiodwave2 = goldenratio[1] * timeperiodwave1
    endwave2 = startwave2 + timeperiodwave2

    # Calculate the third wave

    candlewave3 = candlewave1 + candlewave2
    startwave3 = endwave2
    timeperiodwave3 = goldenratio[3] * timeperiodwave1
    endwave3 = startwave3 - timeperiodwave3

    # Calculate the fourth wave

    candlewave4 = goldenratio[2] * candlewave2
    startwave4 = endwave3
    timeperiodwave4 = goldenratio[0] * timeperiodwave3
    endwave4 = startwave4 + timeperiodwave4

    # Calculate the fifth wave

    candlewave5 = goldenratio[2] * candlewave4
    startwave5 = endwave4
    timeperiodwave5 = timeperiodwave1
    endwave5 = startwave5 - timeperiodwave5

    # Calculate A

    wavesum = candlewave1 + candlewave2 + candlewave3 + candlewave4 + candlewave5
    candlewavea = (wavesum / 2) / 2.618
    startwavea = endwave5
    timeperiodwavea = goldenratio[0] * timeperiodwave5
    endwavea = startwavea + timeperiodwavea

    # Calculate B

    candlewaveb = goldenratio[1] * candlewavea
    startwaveb = endwavea
    timeperiodwaveb = goldenratio[1] * timeperiodwavea
    endwaveb = startwaveb - timeperiodwaveb

    # Calculate C

    candlewavec = candlewavea
    startwavec = endwaveb
    timeperiodwavec = timeperiodwavea
    endwavec = startwavec + timeperiodwavec

    candle = [candlewave1, candlewave2, candlewave3, candlewave4, candlewave5, candlewavea, candlewaveb, candlewavec]
    start = [startwave1, startwave2, startwave3, startwave4, startwave5, startwavea, startwaveb, startwavec]
    end = [endwave1, endwave2, endwave3, endwave4, endwave5, endwavea, endwaveb, endwavec]
    timeperiod = [timeperiodwave1, timeperiodwave2, timeperiodwave3, timeperiodwave4, timeperiodwave5, timeperiodwavea,
                  timeperiodwaveb, timeperiodwavec]

    # for i in range(8) :
    #   print(str(i) + " - "+str(candle[i])+" - "+str(start[i])+" - "+str(end[i])+" - "+str(timeperiod[i])+"\n")
    #   i+=1

    waves = [startwave1, startwave2, startwave3, startwave4, startwave5, startwavea, startwaveb, startwavec, endwavec]
    wavenumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.plot(wavenumbers, waves)
    plt.show()

def bullishtrend():

    candlewave2 = goldenratio[1] * candlewave1
    startwave2 = endwave1
    timeperiodwave2 = goldenratio[1] * timeperiodwave1
    endwave2 = startwave2 - timeperiodwave2

    # Calculate the third wave

    candlewave3 = candlewave1 + candlewave2
    startwave3 = endwave2
    timeperiodwave3 = goldenratio[3] * timeperiodwave1
    endwave3 = startwave3 + timeperiodwave3

    # Calculate the fourth wave

    candlewave4 = goldenratio[2] * candlewave2
    startwave4 = endwave3
    timeperiodwave4 = goldenratio[0] * timeperiodwave3
    endwave4 = startwave4 + timeperiodwave4

    # Calculate the fifth wave

    candlewave5 = goldenratio[2] * candlewave4
    startwave5 = endwave4
    timeperiodwave5 = timeperiodwave1
    endwave5 = startwave5 + timeperiodwave5

    # Calculate A

    wavesum = candlewave1 + candlewave2 + candlewave3 + candlewave4 + candlewave5
    candlewavea = (wavesum / 2) / 2.618
    startwavea = endwave5
    timeperiodwavea = goldenratio[0] * timeperiodwave5
    endwavea = startwavea - timeperiodwavea

    # Calculate B

    candlewaveb = goldenratio[1] * candlewavea
    startwaveb = endwavea
    timeperiodwaveb = goldenratio[1] * timeperiodwavea
    endwaveb = startwaveb + timeperiodwaveb

    # Calculate C

    candlewavec = candlewavea
    startwavec = endwaveb
    timeperiodwavec = timeperiodwavea
    endwavec = startwavec - timeperiodwavec


    candle = [candlewave1, candlewave2, candlewave3, candlewave4, candlewave5, candlewavea, candlewaveb, candlewavec]
    start = [startwave1, startwave2, startwave3, startwave4, startwave5, startwavea, startwaveb, startwavec]
    end = [endwave1, endwave2, endwave3, endwave4, endwave5, endwavea, endwaveb, endwavec]
    timeperiod = [timeperiodwave1, timeperiodwave2, timeperiodwave3, timeperiodwave4, timeperiodwave5, timeperiodwavea,
                  timeperiodwaveb, timeperiodwavec]

    # for i in range(8) :
    #   print(str(i) + " - "+str(candle[i])+" - "+str(start[i])+" - "+str(end[i])+" - "+str(timeperiod[i])+"\n")
    #   i+=1

    waves = [startwave1, startwave2, startwave3, startwave4, startwave5, startwavea, startwaveb, startwavec, endwavec]
    wavenumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.plot(wavenumbers, waves)
    plt.show()

