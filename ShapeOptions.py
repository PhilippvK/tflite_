# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShapeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShapeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsShapeOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ShapeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # ShapeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ShapeOptions
    def OutType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(1)
def ShapeOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddOutType(builder, outType): builder.PrependInt8Slot(0, outType, 0)
def ShapeOptionsAddOutType(builder, outType):
    """This method is deprecated. Please switch to AddOutType."""
    return AddOutType(builder, outType)
def End(builder): return builder.EndObject()
def ShapeOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class ShapeOptionsT(object):

    # ShapeOptionsT
    def __init__(self):
        self.outType = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        shapeOptions = ShapeOptions()
        shapeOptions.Init(buf, pos)
        return cls.InitFromObj(shapeOptions)

    @classmethod
    def InitFromObj(cls, shapeOptions):
        x = ShapeOptionsT()
        x._UnPack(shapeOptions)
        return x

    # ShapeOptionsT
    def _UnPack(self, shapeOptions):
        if shapeOptions is None:
            return
        self.outType = shapeOptions.OutType()

    # ShapeOptionsT
    def Pack(self, builder):
        Start(builder)
        AddOutType(builder, self.outType)
        shapeOptions = End(builder)
        return shapeOptions
