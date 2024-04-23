#pragma once
#include "librarian.h"
namespace Project1 {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;
	using namespace System::Data::SqlClient;

	/// <summary>
	/// Summary for Test
	/// </summary>
	public ref class Test : public System::Windows::Forms::Form
	{
	public:
		Test(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~Test()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::Button^ button1;
	protected:
	private: System::Windows::Forms::TextBox^ textBox1;

	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			this->button1 = (gcnew System::Windows::Forms::Button());
			this->textBox1 = (gcnew System::Windows::Forms::TextBox());
			this->SuspendLayout();
			// 
			// button1
			// 
			this->button1->Location = System::Drawing::Point(131, 262);
			this->button1->Name = L"button1";
			this->button1->Size = System::Drawing::Size(75, 23);
			this->button1->TabIndex = 0;
			this->button1->Text = L"button1";
			this->button1->UseVisualStyleBackColor = true;
			this->button1->Click += gcnew System::EventHandler(this, &Test::button1_Click);
			// 
			// textBox1
			// 
			this->textBox1->Location = System::Drawing::Point(95, 139);
			this->textBox1->Name = L"textBox1";
			this->textBox1->Size = System::Drawing::Size(149, 22);
			this->textBox1->TabIndex = 1;
			// 
			// Test
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(8, 16);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->ClientSize = System::Drawing::Size(503, 382);
			this->Controls->Add(this->textBox1);
			this->Controls->Add(this->button1);
			this->Margin = System::Windows::Forms::Padding(4, 4, 4, 4);
			this->Name = L"Test";
			this->Text = L"Test";
			this->ResumeLayout(false);
			this->PerformLayout();

		}

	public: librarian^ libw;

#pragma endregion
	private: System::Void button1_Click(System::Object^ sender, System::EventArgs^ e) {
		String^ NAME = this->textBox1->Text;

		try {
			String^ connString = "Data Source=DESKTOP-IEDJR1O\\THIRD;Initial Catalog=lms3;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False";
			SqlConnection sqlconn(connString);
			sqlconn.Open();

			String^ sqlquery = "SELECT * FROM Librarian WHERE NAME=@NAME ; ";
			SqlCommand command(sqlquery, %sqlconn);
			command.Parameters->AddWithValue("@NAME", NAME);

			SqlDataReader^ reader = command.ExecuteReader();

			if (reader->Read()) {
				libw = gcnew librarian;
				libw->Staff_ID = reader->GetInt32(0);
				libw->NAME = reader->GetString(1);
				libw->password = reader->GetString(2);
				libw->Email_address = reader->GetString(3);
				MessageBox::Show("succ");
				this->Close();
			}
			else {
				MessageBox::Show("failed");
			}
		}
		catch (Exception^ e) {
			MessageBox::Show("error " + e);
		}
	}
		  
	};
}
