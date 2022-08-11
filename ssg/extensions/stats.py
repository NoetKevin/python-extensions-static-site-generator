import time


from ssg import hooks


start_time = None
total_written = 0

@stats.register("start_build")
def start_build():
    global start_time = time()


@stats.register("written")
def written():
    global total_written += 1

@stats.register("stats")
def stats():
    global start_time
    final_time = time() - start_time
    average = if total_written != 0 : final_time / total_written
    report = "Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"
    print (report.format(total_written, final_time, average))
