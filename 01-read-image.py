import cv2


img = cv2.imread("resources/1.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)


# [vim-hug-neovim-rpc] Vim(pythonx):Traceback (most recent call last):
# Error detected while processing function deoplete#enable[9]..deoplete#initialize[1]..deoplete#init#_initialize[10]..<SNR>20_init_internal_varia
# bles[28]..neovim_rpc#serveraddr:
# line   18:
# E605: Exception not caught: [vim-hug-neovim-rpc] requires one of `:pythonx import [pynvim|neovim]` command to work
