#include <string>
#include <iostream>

#include <XdgUtils/DesktopEntry/DesktopEntry.h>
#include <XdgUtils/BaseDir/BaseDir.h>

int main() {
    XdgUtils::DesktopEntry::DesktopEntry entry;
    std::cout << "Base dir USER_HOME " << XdgUtils::BaseDir::Home() << std::endl;

    std::cout << "DesktopEntry " << std::endl;
    entry["Desktop Entry/Name"] = "Hello World!";
    std::cout << entry << std::endl;

}
