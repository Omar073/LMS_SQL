#include "Test.h"
using namespace Project1;
using namespace System;
using namespace System::Windows::Forms;
[STAThreadAttribute]
int main(array<String^>^ args) {
    Application::EnableVisualStyles();
    Application::SetCompatibleTextRenderingDefault(false);
    Project1::Test form;
    Application::Run(% form);
    form.ShowDialog();
    librarian^ libw = form.libw;

    if (libw != nullptr) {
        MessageBox::Show("succ");
    }



    
}