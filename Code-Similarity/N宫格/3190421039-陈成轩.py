import locale
import ctypes
import re
import ctypes.wintypes
from ctypes import windll

DEFAULT_CODING = locale.getpreferredencoding()

windll.kernel32.WriteProcessMemory.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
]

windll.kernel32.ReadProcessMemory.argtypes = (
    ctypes.wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
)


class ProcessEntry32(ctypes.Structure):
    _fields_ = [
        ('dwSize', ctypes.c_ulong),
        ('cntUsage', ctypes.c_ulong),
        ('th32ProcessID', ctypes.c_ulong),
        ('th32DefaultHeapID', ctypes.POINTER(ctypes.c_ulong)),
        ('th32ModuleID', ctypes.c_ulong),
        ('cntThreads', ctypes.c_ulong),
        ('th32ParentProcessID', ctypes.c_ulong),
        ('pcPriClassBase', ctypes.c_ulong),
        ('dwFlags', ctypes.c_ulong),
        ('szExeFile', ctypes.c_char * ctypes.wintypes.MAX_PATH)
    ]

    def __init__(self, *args, **kwds):
        super(ProcessEntry32, self).__init__(*args, **kwds)
        self.dwSize = ctypes.sizeof(self)


class MODULEINFO(ctypes.Structure):
    _fields_ = [
        ("lpBaseOfDll", ctypes.c_void_p),  # remote pointer
        ("SizeOfImage", ctypes.c_ulong),
        ("EntryPoint", ctypes.c_void_p),  # remote pointer
    ]


def list_processes():
    windll.kernel32.SetLastError(0)
    hSnap = windll.kernel32.CreateToolhelp32Snapshot(0x00000002, 0)
    process_entry = ProcessEntry32()
    process_entry.dwSize = ctypes.sizeof(process_entry)
    p32 = windll.kernel32.Process32First(hSnap, ctypes.byref(process_entry))
    if p32:
        yield process_entry
    while p32:
        yield process_entry
        p32 = windll.kernel32.Process32Next(hSnap, ctypes.byref(process_entry))
    windll.kernel32.CloseHandle(hSnap)


def find_text(pe):
    for sect in pe.sections:
        if sect.Name.startswith(b'.text'):
            return sect


def main():
    patch_byte = b'\x2e' if input('输入1打补丁，不输入恢复>>') else b'\x04'
    for p in list_processes():
        if 'ffxiv_dx11.exe' in p.szExeFile.decode(DEFAULT_CODING).lower():
            handle = windll.kernel32.OpenProcess(0x1F0FFF, False, p.th32ProcessID)
            if not handle: raise Exception('OpenProcess failed, error code: %d' % windll.kernel32.GetLastError())
            buffer = ctypes.create_string_buffer(ctypes.wintypes.MAX_PATH)
            windll.kernel32.SetLastError(0)
            rl = windll.psapi.GetModuleFileNameExA(handle, None, ctypes.byref(buffer), ctypes.wintypes.MAX_PATH)
            if not rl: raise Exception('GetModuleFileName failed with error code %d' % windll.kernel32.GetLastError())
            executable = buffer.value.decode(DEFAULT_CODING)
            hModules = (ctypes.c_void_p * 1)()
            if not windll.psapi.EnumProcessModulesEx(handle, ctypes.byref(hModules), 8, ctypes.byref(ctypes.c_ulong()), 0x02):
                raise Exception('EnumProcessModulesEx failed with error code %d' % windll.kernel32.GetLastError())
            module_info = MODULEINFO()
            if not windll.psapi.GetModuleInformation(handle, ctypes.c_void_p(hModules[0]), ctypes.byref(module_info), ctypes.sizeof(module_info)):
                raise Exception('GetModuleInformation failed with error code %d' % windll.kernel32.GetLastError())
            module_data = (ctypes.c_ubyte * module_info.SizeOfImage)()
            if not windll.kernel32.ReadProcessMemory(handle, module_info.lpBaseOfDll, ctypes.byref(module_data), ctypes.sizeof(module_data), None):
                raise Exception('ReadProcessMemory failed with error code %d' % windll.kernel32.GetLastError())
            match = re.search(b'.\x32\xdb\xeb.\x48\x8b\x01', bytes(module_data))
            if not match: raise Exception('Cannot find target bytes in %s' % executable)
            if not windll.kernel32.WriteProcessMemory(handle, match.span()[0] + module_info.lpBaseOfDll, patch_byte, 1, None):
                raise Exception('WriteProcessMemory failed with error code %d' % windll.kernel32.GetLastError())
            print("patch"if patch_byte == b'\x2e' else "unpatch", p.th32ProcessID)
            windll.kernel32.CloseHandle(handle)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        input('Press any key to exit...')
