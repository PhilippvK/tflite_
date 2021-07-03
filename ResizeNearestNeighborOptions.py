# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ResizeNearestNeighborOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ResizeNearestNeighborOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsResizeNearestNeighborOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ResizeNearestNeighborOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # ResizeNearestNeighborOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ResizeNearestNeighborOptions
    def AlignCorners(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ResizeNearestNeighborOptions
    def HalfPixelCenters(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(2)
def ResizeNearestNeighborOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddAlignCorners(builder, alignCorners): builder.PrependBoolSlot(0, alignCorners, 0)
def ResizeNearestNeighborOptionsAddAlignCorners(builder, alignCorners):
    """This method is deprecated. Please switch to AddAlignCorners."""
    return AddAlignCorners(builder, alignCorners)
def AddHalfPixelCenters(builder, halfPixelCenters): builder.PrependBoolSlot(1, halfPixelCenters, 0)
def ResizeNearestNeighborOptionsAddHalfPixelCenters(builder, halfPixelCenters):
    """This method is deprecated. Please switch to AddHalfPixelCenters."""
    return AddHalfPixelCenters(builder, halfPixelCenters)
def End(builder): return builder.EndObject()
def ResizeNearestNeighborOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class ResizeNearestNeighborOptionsT(object):

    # ResizeNearestNeighborOptionsT
    def __init__(self):
        self.alignCorners = False  # type: bool
        self.halfPixelCenters = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        resizeNearestNeighborOptions = ResizeNearestNeighborOptions()
        resizeNearestNeighborOptions.Init(buf, pos)
        return cls.InitFromObj(resizeNearestNeighborOptions)

    @classmethod
    def InitFromObj(cls, resizeNearestNeighborOptions):
        x = ResizeNearestNeighborOptionsT()
        x._UnPack(resizeNearestNeighborOptions)
        return x

    # ResizeNearestNeighborOptionsT
    def _UnPack(self, resizeNearestNeighborOptions):
        if resizeNearestNeighborOptions is None:
            return
        self.alignCorners = resizeNearestNeighborOptions.AlignCorners()
        self.halfPixelCenters = resizeNearestNeighborOptions.HalfPixelCenters()

    # ResizeNearestNeighborOptionsT
    def Pack(self, builder):
        Start(builder)
        AddAlignCorners(builder, self.alignCorners)
        AddHalfPixelCenters(builder, self.halfPixelCenters)
        resizeNearestNeighborOptions = End(builder)
        return resizeNearestNeighborOptions
