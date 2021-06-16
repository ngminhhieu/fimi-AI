import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import datetime


fimi01 = pd.read_csv('./app/data/fimi01_new.csv')
fimi02 = pd.read_csv('./app/data/fimi02_new.csv')
envitus = pd.read_csv('./app/data/envitus_new.csv')
fimi01['datetime'] = pd.to_datetime(fimi01['datetime'])
fimi02['datetime'] = pd.to_datetime(fimi02['datetime'])
envitus['datetime'] = pd.to_datetime(envitus['datetime']) + datetime.timedelta(hours=7)

fig, axs = plt.subplots(3)
fig.suptitle('Data trong khoang thoi gian thi nghiem voi thay Thuan')
axs[0].plot(fimi01['datetime'], fimi01['pm2_5'])
axs[0].set_title("Fimi01")
axs[0].axes.xaxis.set_visible(False)

axs[1].plot(fimi02['datetime'], fimi02['pm2_5'])
axs[1].set_title("Fimi02")
axs[1].axes.xaxis.set_visible(False)

axs[2].plot(envitus['datetime'], envitus['pm2_5'])
axs[2].set_title("Envitus")
axs[2].axes.xaxis.set_visible(False)
for ax in axs.flat:
    ax.set(xlabel='Datetime', ylabel='PM2.5')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.show()

plt.plot(fimi01['datetime'], fimi01['pm2_5'], label = "fimi01", color='green')
plt.plot(fimi02['datetime'], fimi02['pm2_5'], label = "fimi02", color='red')
plt.plot(envitus['datetime'], envitus['pm2_5'], label = "envitus", color='blue')
plt.xlabel('datetime')
plt.ylabel('pm2.5')
plt.title('Data trong khoang thoi gian thi nghiem voi thay Thuan')
plt.legend()
plt.show()



fimi01['pm2_5'] = savgol_filter(fimi01['pm2_5'], 101, 3)
fimi02['pm2_5'] = savgol_filter(fimi02['pm2_5'], 51, 3)
envitus['pm2_5'] = savgol_filter(envitus['pm2_5'], 11, 3)

fig, axs = plt.subplots(3)
fig.suptitle('Data trong khoang thoi gian thi nghiem voi thay Thuan (Smooth)')
axs[0].plot(fimi01['datetime'], fimi01['pm2_5'])
axs[0].set_title("Fimi01")
axs[0].axes.xaxis.set_visible(False)

axs[1].plot(fimi02['datetime'], fimi02['pm2_5'])
axs[1].set_title("Fimi02")
axs[1].axes.xaxis.set_visible(False)

axs[2].plot(envitus['datetime'], envitus['pm2_5'])
axs[2].set_title("Envitus")
axs[2].axes.xaxis.set_visible(False)
for ax in axs.flat:
    ax.set(xlabel='Datetime', ylabel='PM2.5')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.show()


plt.plot(fimi01['datetime'], fimi01['pm2_5'], label = "fimi01", color='green')
plt.plot(fimi02['datetime'], fimi02['pm2_5'], label = "fimi02", color='red')
plt.plot(envitus['datetime'], envitus['pm2_5'], label = "envitus", color='blue')
plt.xlabel('datetime')
plt.ylabel('pm2.5')
plt.title('Data trong khoang thoi gian thi nghiem voi thay Thuan (Smooth)')
plt.legend()
plt.show()

# fimi01 = fimi01.resample('1min', on='datetime').mean()
# fimi02 = fimi02.resample('1min', on='datetime').mean()
# envitus = envitus.resample('1min', on='datetime').mean()


# fig, axs = plt.subplots(3)
# fig.suptitle('Data thu trong khoang thoi gian thi nghiem voi thay Thuan')
# axs[0].plot(fimi01.index, fimi01['pm2_5'])
# axs[0].set_title("Fimi01")
# axs[0].axes.xaxis.set_visible(False)

# axs[1].plot(fimi02.index, fimi02['pm2_5'])
# axs[1].set_title("Fimi02")
# axs[1].axes.xaxis.set_visible(False)

# axs[2].plot(envitus.index, envitus['pm2_5'])
# axs[2].set_title("Envitus")
# axs[2].axes.xaxis.set_visible(False)
# for ax in axs.flat:
#     ax.set(xlabel='Datetime', ylabel='PM2.5')

# # Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()
# plt.show()