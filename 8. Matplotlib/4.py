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


def update(val):
    ax_sum.clear()
    x = np.linspace(0, 10, 1000)
    y1 = amp1 * np.sin(2 * np.pi * freq1 * x)
    y2 = amp2 * np.sin(2 * np.pi * freq2 * x)

    ax_wave1.plot(x, y1, 'r')
    ax_wave2.plot(x, y2, 'b')

    y_sum = y1 + y2
    ax_sum.plot(x, y_sum, 'g')

    ax_wave1.set_title(f'Wave 1 (Freq: {freq1}, Amp: {amp1})')
    ax_wave2.set_title(f'Wave 2 (Freq: {freq2}, Amp: {amp2})')
    ax_sum.set_title('Sum of Waves')

    plt.draw()



axfreq1 = plt.axes([0.1, 0.15, 0.7, 0.03])
axamp1 = plt.axes([0.1, 0.2, 0.7, 0.03])
axfreq2 = plt.axes([0.1, 0.05, 0.7, 0.03])
axamp2 = plt.axes([0.1, 0.1, 0.7, 0.03])

sfreq1 = Slider(axfreq1, 'Freq 1', 0.1, 5.0, valinit=freq1)
samp1 = Slider(axamp1, 'Amp 1', 0.1, 2.0, valinit=amp1)
sfreq2 = Slider(axfreq2, 'Freq 2', 0.1, 5.0, valinit=freq2)
samp2 = Slider(axamp2, 'Amp 2', 0.1, 2.0, valinit=amp2)

sfreq1.on_changed(lambda x: update(None))
samp1.on_changed(lambda x: update(None))
sfreq2.on_changed(lambda x: update(None))
samp2.on_changed(lambda x: update(None))

update(None)
plt.show()
