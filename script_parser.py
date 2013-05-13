"""
Contains code for parsing script files (be they text
files or binary dumps), and for representing them
(like DAOs).
"""

class ScriptFileParser(object):
    """
    All classes the will parse script files must extend this
    class. This class loads one field, self.script_file,
    which is a reference to the open script file.

    In addition to self.script_file, the following fields
    are also provided, but are not filled: stx, etx, separator,
    and a list of the packets that follow.

    After initializing a ScriptFileParser object, no further
    method calls should be necessary; the fields should be
    automatically initialized.
    """
    
    def __init__(self, filename):
        """
        Opens the script file in described by filename.
        """
        self.script_file = open(filename)
        self.stx = ""
        self.etx = ""
        self.separator = ""
        self.packet_list = []

class TextScriptParser(ScriptFileParser):
    """
    Note that, though this still follows the specified convention
    of the first line being the separator byte, this is ignored
    by TextScriptParser and uses the newline character, regardless
    of what is specified in the first line.

    In text file mode, the parsing algorithm will be as follows:
      - The packet list will be one packet per line
      - Every packet sent will be "sandwiched" by the provided packet
        delimiters, whatever they are. The packets in self.packet_list
        are already in this format; no further concatenation needed.
    """
    # TODO Check what happens when using Windows-style pagebreaks.
    
    def __init__(self, filename):
        super(TextScriptParser, self).__init__(filename)
        self.__set_fields()

    def __set_fields(self):
        try:
            # read the first line for the separator
            self.script_file.read()
            # read and parse the second line for the packet delimiters
            delimiters = self.script_file.read()[0:2]
            dellen = len(delimiters)

            if dellen and dellen != 2:
                # TODO Make better Exceptions
                throw Exception("Delimiters line of the script file should have two characters, sans newline.")
            
            self.stx = delimiters[0]
            self.etx = delimiters[1]

            # Get the packet list
            for packet in self.script_file:
                self.packet_list.append(packet)

            self.packet_list = tuple(map(lambda packet: self.stx + packet + self.etx, self.packet_list))
        except Exception, e:
            print(e.message)
        finally:
            self.script_file.close()

class BinaryScriptParser(ScriptFileParser):
    
    def __init__(self, filename):
        super(BinaryScriptParser, self).__init__(filename)
        self.__set_fields()

    def __set_fields(self):
        try:
            # we must be able to read bytes here.
            pass
        except Exception, e:
            print(e.message)
        finally:
            self.script_file.close()
