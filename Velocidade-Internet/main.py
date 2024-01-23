import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    download_speed = st.download() / 1_000_000
    print(f"Velocidade de Download: {download_speed:.2f} Mbps")

    upload_speed = st.upload() / 1_000_000
    print(f"Velocidade de Upload: {upload_speed:.2f} Mbps")

    server = st.get_best_server()
    ping = server["latency"]
    print(f"Ping: {ping} ms")

test_internet_speed()
