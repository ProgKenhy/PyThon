import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, (ax_wave1, ax_wave2, ax_sum) = plt.subplots(3, 1, figsize=(12, 8))
fig.tight_layout(h_pad=3)
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.3, top=0.95)

freq1 = 1.0
amp1 = 1.0
freq2 = 2.0
amp2 = 0.5
x = np.linspace(0, 10, 1000)


def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)


y1 = f(x, amp1, freq1)
y2 = f(x, amp2, freq2)

y_limit = (amp1 + amp2) * 2

ax_wave1.set_ylim(-y_limit, y_limit)
wave1, = ax_wave1.plot(x, y1, 'r')
ax_wave1.grid(True)
ax_wave1.locator_params(nbins=11)

ax_wave2.set_ylim(-y_limit, y_limit)
wave2, = ax_wave2.plot(x, y2, 'b')
ax_wave2.grid(True)
ax_wave2.locator_params(nbins=11)

ax_sum.set_ylim(-y_limit, y_limit)
y_sum = f(x, amp1 + amp2, freq1 + freq2)
sum_wave, = ax_sum.plot(x, y_sum, 'g')
ax_sum.grid(True)
ax_sum.locator_params(nbins=11)
ax_sum.set_title('Sum of Waves')


def update(val):
    new_y1 = f(x, slider_amp1.val, slider_freq1.val)
    wave1.set_ydata(new_y1)

    new_y2 = f(x, slider_amp2.val, slider_freq2.val)
    wave2.set_ydata(new_y2)

    #new_y_sum = f(x, slider_amp1.val + slider_amp2.val, slider_freq1.val + slider_freq2.val)
    new_y_sum = new_y1 + new_y2
    sum_wave.set_ydata(new_y_sum)

    ax_wave1.set_title(f'Wave 1 (Freq: {freq1}, Amp: {amp1})')
    ax_wave2.set_title(f'Wave 2 (Freq: {freq2}, Amp: {amp2})')
    fig.canvas.draw_idle()


axfreq1 = fig.add_axes([0.1, 0.15, 0.7, 0.03])
axamp1 = fig.add_axes([0.1, 0.2, 0.7, 0.03])
axfreq2 = fig.add_axes([0.1, 0.05, 0.7, 0.03])
axamp2 = fig.add_axes([0.1, 0.1, 0.7, 0.03])

slider_freq1 = Slider(ax=axfreq1, label='Freq 1', valmin=0, valmax=5.0, valinit=freq1)
slider_amp1 = Slider(ax=axamp1, label='Amp 1', valmin=0, valmax=2.0, valinit=amp1)
slider_freq2 = Slider(axfreq2, 'Freq 2', 0, 5.0, valinit=freq2)
slider_amp2 = Slider(axamp2, 'Amp 2', 0, 2.0, valinit=amp2)

slider_freq1.on_changed(update)
slider_amp1.on_changed(update)
slider_freq2.on_changed(update)
slider_amp2.on_changed(update)


plt.show()
