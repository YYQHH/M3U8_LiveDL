# -*- coding: utf-8 -*-
import os
import subprocess
import signal
import threading
import keyboard
import time
import locale

# 获取系统默认编码
encoding = locale.getpreferredencoding()

def download_m3u8(m3u8_url, output_file):
    log_file = 'ffmpeg_output.log'
    output_dir = os.path.dirname(output_file)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', m3u8_url,
        '-map', '0',  # 匹配所有流
        '-c', 'copy',  # 复制所有流
        '-ignore_unknown',  # 不处理不识别的流
        '-copy_unknown',  # 直接复制字幕流以及其他不识别的流
        output_file
    ]
    
    with open(log_file, 'w', encoding='utf-8') as log:
        process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding=encoding, errors='replace')

        def stop_signal_handler(sig, frame):
            print('Recording stopped by user.')
            process.send_signal(signal.SIGINT)
        
        signal.signal(signal.SIGINT, stop_signal_handler)
        keyboard.add_hotkey('q', stop_signal_handler)

        def print_ffmpeg_output(process):
            while True:
                output = process.stderr.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())
                    log.write(output)
                    log.flush()

        output_thread = threading.Thread(target=print_ffmpeg_output, args=(process,))
        output_thread.start()
        output_thread.join()
    
    return process.wait()

if __name__ == "__main__":
    m3u8_url = input("请输入m3u8地址：")
    output_file = input("请输入输出文件路径（带文件名）：")

    print(f"m3u8 URL: {m3u8_url}")
    print(f"Output file will be saved to: {output_file}")
    
    start_time = time.time()
    result = download_m3u8(m3u8_url, output_file)
    elapsed_time = time.time() - start_time
    
    if result == 0:
        print(f"Download completed successfully in {elapsed_time:.2f} seconds.")
    else:
        print(f"Download failed with return code {result}.")
        with open('ffmpeg_output.log', 'r', encoding='utf-8') as log:
            print(log.read())