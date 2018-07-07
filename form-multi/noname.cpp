///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Mar  1 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxFlexGridSizer* fgSizer1;
	fgSizer1 = new wxFlexGridSizer( 6, 3, 0, 0 );
	fgSizer1->SetFlexibleDirection( wxBOTH );
	fgSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	
	fgSizer1->Add( 0, 20, 1, wxEXPAND, 5 );
	
	
	fgSizer1->Add( 0, 20, 1, wxEXPAND, 5 );
	
	
	fgSizer1->Add( 0, 20, 1, wxEXPAND, 5 );
	
	
	fgSizer1->Add( 20, 0, 1, wxEXPAND, 5 );
	
	m_staticText3 = new wxStaticText( this, wxID_ANY, wxT("Valor1"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3->Wrap( -1 );
	fgSizer1->Add( m_staticText3, 0, wxALL, 5 );
	
	txt1 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( txt1, 0, wxALL, 5 );
	
	
	fgSizer1->Add( 20, 0, 1, wxEXPAND, 5 );
	
	m_staticText31 = new wxStaticText( this, wxID_ANY, wxT("Valor2"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText31->Wrap( -1 );
	fgSizer1->Add( m_staticText31, 0, wxALL, 5 );
	
	txt2 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( txt2, 0, wxALL, 5 );
	
	
	fgSizer1->Add( 20, 0, 1, wxEXPAND, 5 );
	
	m_staticText311 = new wxStaticText( this, wxID_ANY, wxT("Valor3"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText311->Wrap( -1 );
	fgSizer1->Add( m_staticText311, 0, wxALL, 5 );
	
	txt3 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( txt3, 0, wxALL, 5 );
	
	
	fgSizer1->Add( 20, 0, 1, wxEXPAND, 5 );
	
	m_staticText3111 = new wxStaticText( this, wxID_ANY, wxT("Resultado"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3111->Wrap( -1 );
	fgSizer1->Add( m_staticText3111, 0, wxALL, 5 );
	
	txtr = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( txtr, 0, wxALL, 5 );
	
	
	fgSizer1->Add( 20, 0, 1, wxEXPAND, 5 );
	
	m_button2 = new wxButton( this, wxID_ANY, wxT("Procesar"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( m_button2, 0, wxALL, 5 );
	
	m_button3 = new wxButton( this, wxID_ANY, wxT("Salir"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( m_button3, 0, wxALL, 5 );
	
	
	this->SetSizer( fgSizer1 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	m_button2->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::evenProcesar ), NULL, this );
	m_button3->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::evetSalir ), NULL, this );
}

MyFrame1::~MyFrame1()
{
	// Disconnect Events
	m_button2->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::evenProcesar ), NULL, this );
	m_button3->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::evetSalir ), NULL, this );
	
}
