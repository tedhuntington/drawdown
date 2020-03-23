import feeder_yahoo
import process
import cache
import plot

#symbols = ['^GSPC', '^BVSP']
symbols = ['^GSPC', '^DJI']
for symbol in symbols:
    data = feeder_yahoo.get_data(symbol)

    crashes = process.crashes(data)
    cache.save_crashes(crashes, symbol)
    plot.crashes(crashes, symbol)

    #drawdown = process.drawdown(data)
    #cache.save_drawdown(drawdown, symbol)
    #plot.drawdown(drawdown, symbol)
