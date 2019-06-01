from ..build import *
from .fpga.lattice_ice40 import LatticeICE40Platform, IceBurnProgrammerMixin


__all__ = ["ICE40HX1KBlinkEVNPlatform"]


class ICE40HX1KBlinkEVNPlatform(IceBurnProgrammerMixin, LatticeICE40Platform):
    device    = "hx1k"
    package   = "vq100"
    clocks    = [
        ("clk3p3", 3.3e6),
    ]
    resources = [
        Resource("clk3p3", 0, Pins("13", dir="i"), extras=["IO_STANDARD=SB_LVCMOS33"]),

        Resource("user_led", 0, Pins("59", dir="o"), extras=["IO_STANDARD=SB_LVCMOS33"]),
        Resource("user_led", 1, Pins("56", dir="o"), extras=["IO_STANDARD=SB_LVCMOS33"]),
        Resource("user_led", 2, Pins("53", dir="o"), extras=["IO_STANDARD=SB_LVCMOS33"]),
        Resource("user_led", 3, Pins("51", dir="o"), extras=["IO_STANDARD=SB_LVCMOS33"]),

        Resource("user_btn", 0, Pins("60"), extras=["IO_STANDARD=SB_LVCMOS33"]),
        Resource("user_btn", 1, Pins("57"), extras=["IO_STANDARD=SB_LVCMOS33"]),
        Resource("user_btn", 2, Pins("54"), extras=["IO_STANDARD=SB_LVCMOS33"]),
        Resource("user_btn", 3, Pins("52"), extras=["IO_STANDARD=SB_LVCMOS33"]),
    ]
