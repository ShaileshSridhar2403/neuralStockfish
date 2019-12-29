#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:38:30 2019

@author: shailesh
"""

import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

board = chess.Board()
counter = 0
while counter<5:
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    print(board);counter+=1
	

engine.quit()