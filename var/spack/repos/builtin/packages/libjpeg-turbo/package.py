from spack import *

class LibjpegTurbo(Package):
    """libjpeg-turbo is a fork of the original IJG libjpeg which uses
       SIMD to accelerate baseline JPEG compression and
       decompression. libjpeg is a library that implements JPEG image
       encoding, decoding and transcoding."""
    homepage = "http://libjpeg-turbo.virtualgl.org"
    url      = "http://sourceforge.net/projects/libjpeg-turbo/files/1.4.2/libjpeg-turbo-1.4.2.tar.gz/download"

    version('1.4.2', '86b0d5f7507c2e6c21c00219162c3c44')

    # Can use either of these.
    depends_on("yasm")
    depends_on("nasm")

    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)

        make()
        make("install")
