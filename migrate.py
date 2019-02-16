#!/usr/bin/env python3
import os
from manage import run
run(os.path.split(__file__)[-1][:-len(".py")].split("_"))
