# -*- encoding: utf-8 -*-
import gi

# import required library like Gstreamer and GstreamerRtspServer
gi.require_version("Gst", "1.0")
gi.require_version("GstRtspServer", "1.0")
from gi.repository import Gst, GLib, GstRtspServer, GObject


if __name__ == "__main__":
    # gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/0 latency=0 ! decodebin ! autovideosink 

    Gst.init(None)

    server = GstRtspServer.RTSPServer.new()
    server.set_service("8554")
    server.connect("client-connected", lambda x1, x2: print(f"Client connected, {x1}, {x2}")) 
    
    factory = GstRtspServer.RTSPMediaFactory.new()
    # gst-launch-1.0 multifilesrc location=../../cclyun/.detect/detect/%06d.jpg loop=true caps="image/jpeg,framerate=\(fraction\)10/1" ! decodebin ! autovideosink
    factory.set_launch("""( 
multifilesrc location=./data/%02d.jpg loop=true caps=image/jpeg,framerate=\(fraction\)10/1 
! jpegparse ! identity sync=true ! jpegdec ! videoconvert ! x264enc ! rtph264pay pt=96 name=pay0 
)""")
    factory.set_shared(True)
    factory.set_transport_mode(GstRtspServer.RTSPTransportMode.PLAY)
    
    mount_points = server.get_mount_points()
    mount_points.add_factory('/0', factory)
    mount_points.add_factory('/1', factory)

    server.attach(None)  
    print("stream ready at rtsp://127.0.0.1:8554/0 and rtsp://127.0.0.1:8554/1")

    GLib.MainLoop().run()
