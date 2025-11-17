"""Auto-generated data models for the TutorCruncher API."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional

from .base import APIModel


@dataclass
class AdhocchargesAdHocChargeObject(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    agent: Optional[AdhocchargesAdHocChargeObjectAgent] = None  # Object of the Agent.
    appointment: Optional[AdhocchargesAdHocChargeObjectAppointment] = None  # Object of the Appointment.
    category: Optional[AdhocchargesAdHocChargeObjectCategory] = None  # Object of the Ad Hoc Charge Category.
    category_id: Optional[int] = None  # Unique identifier for the Ad Hoc Charge Category.
    category_name: Optional[str] = None  # Name for the Ad Hoc Charge Category.
    charge_client_forex: Optional[str] = None  # Amount of money in other currency.
    client_cost: Optional[str] = None  # Amount of money in the Branch's currency.
    client: Optional[AdhocchargesAdHocChargeObjectClient] = None  # Object of the Client.
    contractor: Optional[AdhocchargesAdHocChargeObjectContractor] = None  # Object to the Contractor.
    creator: Optional[AdhocchargesAdHocChargeObjectCreator] = None  # User who created the Ad Hoc Charge.
    currency: Optional[str] = None  # The currency used.
    currency_conversion: Optional[str] = None  # Currency conversion at the time the Ad Hoc Charge was created.
    date_occurred: Optional[str] = None  # Date and time the Ad Hoc Charge was created.
    invoices: List[AdhocchargesAdHocChargeObjectInvoicesItem] = field(default_factory=list)  # An array of Invoices the Ad Hoc Charge appears on.
    payment_orders: List[AdhocchargesAdHocChargeObjectPaymentOrdersItem] = field(default_factory=list)  # An array of Payment Orders the Ad Hoc Charge appears on.
    net_gross: Optional[str] = None  # Whether the Ad Hoc Charge is `net` or `gross`.
    pay_contractor: Optional[str] = None  # Amount the Contractor will be paid.
    service: Optional[AdhocchargesAdHocChargeObjectService] = None  # Object of the Service related to the Ad Hoc Charge.
    tax_amount: Optional[Decimal] = None  # Amount of tax on the Ad Hoc Charge.

@dataclass
class AdhocchargesAdHocChargeObjectAgent(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectAgent."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class AdhocchargesAdHocChargeObjectAppointment(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectAppointment."""
    id: Optional[int] = None  # Unique identifier for the object.
    start: Optional[str] = None  # Start date and time for the Appointment.
    finish: Optional[str] = None  # Finish date and time for the Appointment.
    topic: Optional[str] = None  # Topic for the Appointment.
    status: Optional[int] = None  # The status for the Appointment, the choices are:  - `10` for Planned - `15` for Awaiting Report - `20` for Complete - `30` for Cancelled - `40` for Cancelled but Chargeable
    service: Optional[Dict[str, Any]] = None  # Object that contains information about the Service. Attributes in the object are `id`, `name`,  `dft_charge_type`, `created`, `dft_charge_rate`, `dft_conractor_rate`, `last_updated`, `status`, `url`.
    url: Optional[str] = None  # URL to the Appointment object.

@dataclass
class AdhocchargesAdHocChargeObjectCategory(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectCategory."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the Ad Hoc Charge Category.
    branch_tax_setup: Optional[str] = None  # Tax setup for the Branch when invoicing.
    contractor_tax_setup: Optional[str] = None  # Tax setup for the Contractors when invoicing.
    contractor_usable: Optional[bool] = None  # If Contractors can use the category for expenses.
    default_charge_amount: Optional[Decimal] = None  # Default charge_client amount for the Ad Hoc Charge Category.
    default_description: Optional[str] = None  # Default description for the Ad Hoc Charge Category.
    default_pay_amount: Optional[Decimal] = None  # Default pay_contractor amount for the Ad Hoc Charge Category.
    dft_net_gross: Optional[str] = None  # Default net/gross value for the Ad Hoc Charge Category.

@dataclass
class AdhocchargesAdHocChargeObjectClient(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectClient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Client's object.

@dataclass
class AdhocchargesAdHocChargeObjectContractor(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectContractor."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Contractor's object.

@dataclass
class AdhocchargesAdHocChargeObjectCreator(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectCreator."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.

@dataclass
class AdhocchargesAdHocChargeObjectInvoicesItem(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectInvoicesItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    display_id: Optional[str] = None  # The Invoice's display ID.
    date_sent: Optional[str] = None  # Date and time the Invoice was sent.
    gross: Optional[str] = None  # Gross amount for the Invoice.
    net: Optional[Decimal] = None  # Net amount for the Invoice.
    tax: Optional[str] = None  # Tax amount for the Invoice.
    client: Optional[Dict[str, Any]] = None  # Object of the Client on the Invoice. Contains their `id`, `first_name`, `last_name`, `email`, and `url`.
    status: Optional[str] = None  # The status of the Invoice. Check out [Invoice Object](#invoice-object) for the types of statuses.
    url: Optional[str] = None  # The URL to the Invoice object.

@dataclass
class AdhocchargesAdHocChargeObjectPaymentOrdersItem(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectPaymentOrdersItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    display_id: Optional[str] = None  # The Payment Order's display ID.
    gross: Optional[str] = None  # Gross amount for the Payment Order.
    net: Optional[Decimal] = None  # Net amount for the Payment Order.
    tax: Optional[str] = None  # Tax amount for the Invoice.
    payee: Optional[Dict[str, Any]] = None  # Object of the Payee on the Payment Order. Contains their `id`, `first_name`, `last_name`, `email`, and `url`.
    status: Optional[str] = None  # The status of the Payment Order. Check out [Payment Order Object](#payment-order-object) for the types of statuses.

@dataclass
class AdhocchargesAdHocChargeObjectService(APIModel):
    """Auto-generated model for AdhocchargesAdHocChargeObjectService."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Service's name.
    dft_charge_type: Optional[str] = None  # Service's default charge type. Check out [Service Object](#service-object) for the types of choices.
    created: Optional[str] = None  # Date and time the Service was created.
    dft_charge_rate: Optional[str] = None  # Service's default amount Clients will be charged.
    dft_contractor_rate: Optional[str] = None  # Service's default amount Contractors will be paided.
    status: Optional[str] = None  # Status of the Service. Check out [Service Object](#service-object) for the types of statuses.
    url: Optional[str] = None  # URL to the Service object.

@dataclass
class AhcCategoriesAdHocChargeCategoryObject(APIModel):
    """Auto-generated model for AhcCategoriesAdHocChargeCategoryObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the Ad Hoc Charge Category.
    branch_tax_setup: Optional[str] = None  # Tax setup for the Branch when invoicing.
    contractor_tax_setup: Optional[str] = None  # Tax setup for the Contractors when invoicing.
    contractor_usable: Optional[bool] = None  # If Contractors can use the category for expenses.
    default_charge_amount: Optional[Decimal] = None  # Default charge_client amount for the Ad Hoc Charge Category.
    default_description: Optional[str] = None  # Default description for the Ad Hoc Charge Category.
    default_pay_amount: Optional[Decimal] = None  # Default pay_contractor amount for the Ad Hoc Charge Category.
    dft_net_gross: Optional[str] = None  # Default net/gross value for the Ad Hoc Charge Category.

@dataclass
class AgentsAgentObjectVersion1(APIModel):
    """Auto-generated model for AgentsAgentObjectVersion1."""
    id: Optional[int] = None  # Unique identifier for the object.
    user: Optional[AgentsAgentObjectVersion1User] = None  # User object containing basic information.
    commission_rate: Optional[str] = None  # Percentage of the Agent's commission rate.
    clients: List[AgentsAgentObjectVersion1ClientsItem] = field(default_factory=list)  # An array of Clients which the Agent is related to.
    last_updated: Optional[str] = None  # The date and time the Agent was last updated.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[AgentsAgentObjectVersion1LabelsItem] = field(default_factory=list)  # An array of the Agent's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`

@dataclass
class AgentsAgentObjectVersion1User(APIModel):
    """Auto-generated model for AgentsAgentObjectVersion1User."""
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.

@dataclass
class AgentsAgentObjectVersion1ClientsItem(APIModel):
    """Auto-generated model for AgentsAgentObjectVersion1ClientsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class AgentsAgentObjectVersion1LabelsItem(APIModel):
    """Auto-generated model for AgentsAgentObjectVersion1LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class AgentsAgentObjectVersion2(APIModel):
    """Auto-generated model for AgentsAgentObjectVersion2."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.
    photo: Optional[str] = None  # The URL to the Agent's photo.
    commission_rate: Optional[str] = None  # Percentage of the Agent's commission rate.
    clients: List[AgentsAgentObjectVersion2ClientsItem] = field(default_factory=list)  # An array of Clients which the Agent is related to.
    last_updated: Optional[str] = None  # The date and time the Agent was last updated.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[AgentsAgentObjectVersion2LabelsItem] = field(default_factory=list)  # An array of the Agent's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`

@dataclass
class AgentsAgentObjectVersion2ClientsItem(APIModel):
    """Auto-generated model for AgentsAgentObjectVersion2ClientsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class AgentsAgentObjectVersion2LabelsItem(APIModel):
    """Auto-generated model for AgentsAgentObjectVersion2LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class AppointmentsAppointmentObject(APIModel):
    """Auto-generated model for AppointmentsAppointmentObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    start: Optional[str] = None  # Appointment's start date and time.
    finish: Optional[str] = None  # Appointment's finish date and time.
    units: Optional[str] = None  # If charge type `hourly`, units will be the length of the Appointment divided by an hour.
    topic: Optional[str] = None  # Appointment's topic.
    location: Optional[AppointmentsAppointmentObjectLocation] = None  # Object of the Appointment's Location.
    rcras: List[AppointmentsAppointmentObjectRcrasItem] = field(default_factory=list)  # An array of Recipients that are on the Appointment.
    cjas: List[AppointmentsAppointmentObjectCjasItem] = field(default_factory=list)  # An array of Contractors that are on the Appointment.
    status: Optional[str] = None  # The status for the Appointment, the status types are `planned`, `awaiting-report`, `complete`, `cancelled`, and `cancelled-chargeable`.
    repeater: Optional[AppointmentsAppointmentObjectRepeater] = None  # Object about the Appointment's repeating appointments.

@dataclass
class AppointmentsAppointmentObjectLocation(APIModel):
    """Auto-generated model for AppointmentsAppointmentObjectLocation."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Location's name.
    description: Optional[str] = None  # Location's description.
    can_conflict: Optional[bool] = None  # Whether the location can conflict with other Appointment's at similar time.
    role: Optional[int] = None  # Unique identifier of the related User to the location.
    latitute: Optional[str] = None  # Location's latitude.
    longitude: Optional[str] = None  # Location's longitude.
    address: Optional[str] = None  # Location's full address.

@dataclass
class AppointmentsAppointmentObjectRcrasItem(APIModel):
    """Auto-generated model for AppointmentsAppointmentObjectRcrasItem."""
    recipient: Optional[int] = None  # Unique identifier of the Recipient.
    recipient_name: Optional[str] = None  # Name of the recipient.
    paying_client: Optional[int] = None  # Unique identifier of the Paying Client for the Recipient.
    paying_client_name: Optional[str] = None  # Name of the Paying Client.
    charge_rate: Optional[str] = None  # Amount the Client will be charged.
    status: Optional[str] = None  # The status of the student for that Appointment. Normally is attended, but can be different for group lessons where one or more students might have cancelled/not turned up but the Appointment still went ahead. This field is currently `read_only`, and cannot be changed through the API. If you would like this to change, please email devteam@tutorcruncher.com.

@dataclass
class AppointmentsAppointmentObjectCjasItem(APIModel):
    """Auto-generated model for AppointmentsAppointmentObjectCjasItem."""
    contractor: Optional[int] = None  # Unique identifier of the Contractor.
    contractor_name: Optional[str] = None  # Name of the Contractor.
    pay_rate: Optional[str] = None  # Amount the Contractor will be charged.

@dataclass
class AppointmentsAppointmentObjectRepeater(APIModel):
    """Auto-generated model for AppointmentsAppointmentObjectRepeater."""
    repeat: Optional[str] = None  # Type of repeater, types are `Daily` or `Weekly`.
    every: Optional[int] = None  # How often it will repeat lessons, every X days/weeks.
    repeat_on: Optional[str] = None  # List of days the repeater will add Appointments on.
    stops_on: Optional[str] = None  # Date the repeater will stop adding Appointments.
    stops_after: Optional[int] = None  # Max amount of Appointments that will be created.
    source_apt: Optional[int] = None  # Unique identifier of the Appointment which the repeater is repeating from.
    service: Optional[Dict[str, Any]] = None  # Object that contains information about the Service. Attributes in the object are `id`, `name`,  `dft_charge_type`, `created`, `dft_charge_rate`, `dft_conractor_rate`, `last_updated`, `status`, `url`.
    charge_type: Optional[str] = None  # How the Appointment will be charged. Types are `Hourly` or `One off`.

@dataclass
class BalanceUpdatesBalanceUpdateObject(APIModel):
    """Auto-generated model for BalanceUpdatesBalanceUpdateObject."""
    id: Optional[int] = None  # Unique identifier for the balance update.
    created: Optional[datetime] = None  # The date and time when the balance update was created.
    creator: Optional[BalanceUpdatesBalanceUpdateObjectCreator] = None  # The user who created this balance update.
    credit_amount: Optional[Decimal] = None  # The amount of credit being added or removed from the client's balance.
    description: Optional[str] = None  # A description explaining the reason for the balance update.
    method: Optional[str] = None  # The payment method used for the balance update. Options for this field are ['cash', 'cheque', 'credit_card', 'transferwise', 'debit_card', 'bank_transfer', 'direct_debit', 'bonus_credit', 'manual', 'voucher', 'correction'].
    related_item: Optional[Dict[str, Any]] = None  # Any related object that this balance update is associated with (nullable).
    role: Optional[BalanceUpdatesBalanceUpdateObjectRole] = None  # The user whose balance is being updated.
    update_type: Optional[str] = None  # The type of update being performed (e.g., "via_api", "manual").

@dataclass
class BalanceUpdatesBalanceUpdateObjectCreator(APIModel):
    """Auto-generated model for BalanceUpdatesBalanceUpdateObjectCreator."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # The User's first name.
    last_name: Optional[str] = None  # The User's last name.
    email: Optional[str] = None  # The User's email address.
    role_type: Optional[str] = None  # The role type of the Balance Update creator.
    url: Optional[str] = None  # URL to the Creator's object. (This field will not be present if the creator is an Administrator)

@dataclass
class BalanceUpdatesBalanceUpdateObjectRole(APIModel):
    """Auto-generated model for BalanceUpdatesBalanceUpdateObjectRole."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    role_type: Optional[str] = None  # The role type of the User.
    url: Optional[str] = None  # URL to the User's object.

@dataclass
class BranchBranchObject(APIModel):
    """Auto-generated model for BranchBranchObject."""
    id: Optional[int] = None  # Unique identifier for the Branch object.
    agency: Optional[BranchBranchObjectAgency] = None  # Object of the agency associated with the branch.
    country: Optional[str] = None  # The country where the branch is located.
    created: Optional[str] = None  # Date and time when the branch was created.
    currency: Optional[str] = None  # The currency used in the branch.
    datetime_output_formats: Optional[BranchBranchObjectDatetimeOutputFormats] = None  # Object containing the datetime output formats for the branch.
    demo: Optional[bool] = None  # If `True`, the branch is a demo branch.
    longitude: Optional[float] = None  # The longitude of the branch location.
    latitude: Optional[float] = None  # The latitude of the branch location.
    name: Optional[str] = None  # The name of the branch.
    page_logo: Optional[str] = None  # The URL of the branch's logo.
    phone: Optional[str] = None  # The phone number of the branch.
    postcode: Optional[str] = None  # The postcode of the branch.
    street: Optional[str] = None  # The street address of the branch.
    timezone: Optional[str] = None  # The timezone of the branch.
    town: Optional[str] = None  # The town of the branch.
    website: Optional[str] = None  # The website of the branch.

@dataclass
class BranchBranchObjectAgency(APIModel):
    """Auto-generated model for BranchBranchObjectAgency."""
    id: Optional[int] = None  # Unique identifier for the agency object.
    blurb: Optional[str] = None  # Brief description of the agency.
    created: Optional[str] = None  # Date and time when the agency was created.
    login_url: Optional[str] = None  # URL to the agency's login page.
    name: Optional[str] = None  # The name of the agency.
    status: Optional[str] = None  # Status of the agency, choices are `active-paying`, `active-not-paying`, `archived`, or `deleted`.
    url_slug: Optional[str] = None  # The URL slug for the agency.

@dataclass
class BranchBranchObjectDatetimeOutputFormats(APIModel):
    """Auto-generated model for BranchBranchObjectDatetimeOutputFormats."""
    date_name: Optional[str] = None  # The date format for display.
    dj_date: List[Any] = field(default_factory=list)  # Array of Django date formats.
    mt_date: Optional[str] = None  # Moment.js date format.
    tpl_date: Optional[str] = None  # The date format for templates.
    time_name: Optional[str] = None  # The time format for display.
    dj_time: List[Any] = field(default_factory=list)  # Array of Django time formats.
    mt_time: Optional[str] = None  # Moment.js time format.
    tpl_time: Optional[str] = None  # The time format for templates.
    tpl_datetime: Optional[str] = None  # The datetime format for templates.
    tpl_datetime_short: Optional[str] = None  # The short datetime format for templates.
    day_first: Optional[bool] = None  # If `True`, the day comes before the month in date formats.
    cal_date_display: Optional[str] = None  # The date format for the calendar.
    display_input: Optional[str] = None  # The datetime format for display.
    dj_datetime: List[Any] = field(default_factory=list)  # Array of Django datetime formats.
    mt_datetime: Optional[str] = None  # Moment.js datetime format.
    datetime_name: Optional[str] = None  # The datetime format for display.

@dataclass
class ClientsClientObjectVersion1(APIModel):
    """Auto-generated model for ClientsClientObjectVersion1."""
    id: Optional[int] = None  # Unique identifier for the object.
    user: Optional[ClientsClientObjectVersion1User] = None  # User object containing basic information.
    status: Optional[str] = None  # The Client's status, choices are `prospect`, `live` and `dormant`.
    is_taxable: Optional[bool] = None  # Whether or not tax should be paid on payments from this Client.
    received_notifications: List[Any] = field(default_factory=list)  # An array of the Client's received notifications. choices are `broadcasts`, `apt_reminders`, `low_balance_reminders`, `invoice_reminders`, `pfi_reminders`, `invoices`, `credit_requests`
    invoices_count: Optional[int] = None  # The number of invoice related to the Client.
    payment_pending: Optional[str] = None  # Total amount of pending payments related to the Client.
    auto_charge: Optional[int] = None  # Whether the Client will be auto charged or not. Choices are `0` to follow the Branch setting, `10` for the Client to be auto charged and `20` for the Client not to be auto charged.
    associated_admin: Optional[ClientsClientObjectVersion1AssociatedAdmin] = None  # Object of the Client Manager.
    associated_agent: Optional[ClientsClientObjectVersion1AssociatedAgent] = None  # Object of the set agent.
    pipeline_stage: Optional[ClientsClientObjectVersion1PipelineStage] = None  # PipelineStage of the client if they are a Prosect client.
    paid_recipients: List[ClientsClientObjectVersion1PaidRecipientsItem] = field(default_factory=list)  # An array of recipients related to the Client.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[ClientsClientObjectVersion1LabelsItem] = field(default_factory=list)  # An array of the Client's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`
    invoice_balance: Optional[str] = None  # The Client's invoice balance.
    available_balance: Optional[str] = None  # The Client's available balance.

@dataclass
class ClientsClientObjectVersion1User(APIModel):
    """Auto-generated model for ClientsClientObjectVersion1User."""
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.

@dataclass
class ClientsClientObjectVersion1AssociatedAdmin(APIModel):
    """Auto-generated model for ClientsClientObjectVersion1AssociatedAdmin."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.

@dataclass
class ClientsClientObjectVersion1AssociatedAgent(APIModel):
    """Auto-generated model for ClientsClientObjectVersion1AssociatedAgent."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class ClientsClientObjectVersion1PipelineStage(APIModel):
    """Auto-generated model for ClientsClientObjectVersion1PipelineStage."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # The name of the PipelineStage
    sort_index: Optional[int] = None  # The sort index of the PipelineStage (describes the order of the PipelineStages).

@dataclass
class ClientsClientObjectVersion1PaidRecipientsItem(APIModel):
    """Auto-generated model for ClientsClientObjectVersion1PaidRecipientsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Recipient's object.

@dataclass
class ClientsClientObjectVersion1LabelsItem(APIModel):
    """Auto-generated model for ClientsClientObjectVersion1LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class ClientsClientObjectVersion2(APIModel):
    """Auto-generated model for ClientsClientObjectVersion2."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.
    photo: Optional[str] = None  # The URL to the Client's photo.
    status: Optional[str] = None  # The Client's status, choices are `prospect`, `live` and `dormant`.
    is_taxable: Optional[bool] = None  # Whether or not tax should be paid on payments from this Client.
    received_notifications: List[Any] = field(default_factory=list)  # An array of the Client's received notifications. choices are `broadcasts`, `apt_reminders`, `low_balance_reminders`, `invoice_reminders`, `pfi_reminders`, `invoices`, `credit_requests`
    invoices_count: Optional[int] = None  # The number of invoice related to the Client.
    payment_pending: Optional[str] = None  # Total amount of pending payments related to the Client.
    auto_charge: Optional[int] = None  # Whether the Client will be auto charged or not. Choices are `0` to follow the Branch setting, `10` for the Client to be auto charged and `20` for the Client not to be auto charged.
    associated_admin: Optional[ClientsClientObjectVersion2AssociatedAdmin] = None  # Object of the Client Manager.
    associated_agent: Optional[ClientsClientObjectVersion2AssociatedAgent] = None  # Object of the set agent.
    pipeline_stage: Optional[ClientsClientObjectVersion2PipelineStage] = None  # PipelineStage of the client if they are a Prosect client.
    paid_recipients: List[ClientsClientObjectVersion2PaidRecipientsItem] = field(default_factory=list)  # An array of recipients related to the Client.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[ClientsClientObjectVersion2LabelsItem] = field(default_factory=list)  # An array of the Client's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`
    invoice_balance: Optional[str] = None  # The Client's invoice balance.
    available_balance: Optional[str] = None  # The Client's available balance.

@dataclass
class ClientsClientObjectVersion2AssociatedAdmin(APIModel):
    """Auto-generated model for ClientsClientObjectVersion2AssociatedAdmin."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.

@dataclass
class ClientsClientObjectVersion2AssociatedAgent(APIModel):
    """Auto-generated model for ClientsClientObjectVersion2AssociatedAgent."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class ClientsClientObjectVersion2PipelineStage(APIModel):
    """Auto-generated model for ClientsClientObjectVersion2PipelineStage."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # The name of the PipelineStage
    sort_index: Optional[int] = None  # The sort index of the PipelineStage (describes the order of the PipelineStages).

@dataclass
class ClientsClientObjectVersion2PaidRecipientsItem(APIModel):
    """Auto-generated model for ClientsClientObjectVersion2PaidRecipientsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Recipient's object.

@dataclass
class ClientsClientObjectVersion2LabelsItem(APIModel):
    """Auto-generated model for ClientsClientObjectVersion2LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class ContractorsContractorObjectVersion1(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion1."""
    id: Optional[int] = None  # Unique identifier for the object.
    user: Optional[ContractorsContractorObjectVersion1User] = None  # User object containing basic information.
    status: Optional[str] = None  # The Contractor's status, choices are `pending`, `approved`, `rejected` and `dormant`.
    default_rate: Optional[Decimal] = None  # The Contractor's rate which will be used to override service default rates.
    qualifications: List[ContractorsContractorObjectVersion1QualificationsItem] = field(default_factory=list)  # An array of the Contractor's qualifications.
    skills: List[ContractorsContractorObjectVersion1SkillsItem] = field(default_factory=list)  # An array of the Contractor's skills.
    institutions: List[ContractorsContractorObjectVersion1InstitutionsItem] = field(default_factory=list)  # An array of the Contractor's institutions.
    receive_service_notifications: Optional[bool] = None  # When checked the Tutor will receive email notifications of Jobs available for application.
    review_rating: Optional[Decimal] = None  # Contractor's review rating.
    review_duration: Optional[str] = None  # Total amount of time that has been reviewed.
    last_updated: Optional[str] = None  # The date and time the Contractor was last updated.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[ContractorsContractorObjectVersion1LabelsItem] = field(default_factory=list)  # An array of the Contractor's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`
    work_done_details: Optional[ContractorsContractorObjectVersion1WorkDoneDetails] = None  # Details about the work the Contractor has done.

@dataclass
class ContractorsContractorObjectVersion1User(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion1User."""
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.

@dataclass
class ContractorsContractorObjectVersion1QualificationsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion1QualificationsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    institution: Optional[str] = None  # Name of the institution.
    subject: Optional[str] = None  # Name of the subject.
    qual_level: Optional[str] = None  # Name of the qualification.
    grade: Optional[str] = None  # The grade for the qualification.
    year: Optional[int] = None  # The year for the qualification.
    governing_body: Optional[str] = None  # Name of the governing body for the qualification.

@dataclass
class ContractorsContractorObjectVersion1SkillsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion1SkillsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    subject: Optional[str] = None  # Name of the subject.
    qual_level: Optional[str] = None  # Name of the qualification.

@dataclass
class ContractorsContractorObjectVersion1InstitutionsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion1InstitutionsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the institution.

@dataclass
class ContractorsContractorObjectVersion1LabelsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion1LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class ContractorsContractorObjectVersion1WorkDoneDetails(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion1WorkDoneDetails."""
    amount_owed: Optional[Decimal] = None  # The amount of money the Contractor is owed.
    amount_paid: Optional[Decimal] = None  # The amount of money the Contractor has been paid.
    total_paid_hours: Optional[str] = None  # Total amount of time the Contractor has been paid for.

@dataclass
class ContractorsContractorObjectVersion2(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion2."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.
    photo: Optional[str] = None  # The URL to the Contractor's photo.
    status: Optional[str] = None  # The Contractor's status, choices are `pending`, `approved`, `rejected` and `dormant`.
    default_rate: Optional[Decimal] = None  # The Contractor's rate which will be used to override service default rates.
    qualifications: List[ContractorsContractorObjectVersion2QualificationsItem] = field(default_factory=list)  # An array of the Contractor's qualifications.
    skills: List[ContractorsContractorObjectVersion2SkillsItem] = field(default_factory=list)  # An array of the Contractor's skills.
    institutions: List[ContractorsContractorObjectVersion2InstitutionsItem] = field(default_factory=list)  # An array of the Contractor's institutions.
    receive_service_notifications: Optional[bool] = None  # When checked the Tutor will receive email notifications of Jobs available for application.
    review_rating: Optional[Decimal] = None  # Contractor's review rating.
    review_duration: Optional[str] = None  # Total amount of time that has been reviewed.
    last_updated: Optional[str] = None  # The date and time the Contractor was last updated.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[ContractorsContractorObjectVersion2LabelsItem] = field(default_factory=list)  # An array of the Contractor's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`
    work_done_details: Optional[ContractorsContractorObjectVersion2WorkDoneDetails] = None  # Details about the work the Contractor has done.

@dataclass
class ContractorsContractorObjectVersion2QualificationsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion2QualificationsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    institution: Optional[str] = None  # Name of the institution.
    subject: Optional[str] = None  # Name of the subject.
    qual_level: Optional[str] = None  # Name of the qualification.
    grade: Optional[str] = None  # The grade for the qualification.
    year: Optional[int] = None  # The year for the qualification.
    governing_body: Optional[str] = None  # Name of the governing body for the qualification.

@dataclass
class ContractorsContractorObjectVersion2SkillsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion2SkillsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    subject: Optional[str] = None  # Name of the subject.
    qual_level: Optional[str] = None  # Name of the qualification.

@dataclass
class ContractorsContractorObjectVersion2InstitutionsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion2InstitutionsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the institution.

@dataclass
class ContractorsContractorObjectVersion2LabelsItem(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion2LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class ContractorsContractorObjectVersion2WorkDoneDetails(APIModel):
    """Auto-generated model for ContractorsContractorObjectVersion2WorkDoneDetails."""
    amount_owed: Optional[Decimal] = None  # The amount of money the Contractor is owed.
    amount_paid: Optional[Decimal] = None  # The amount of money the Contractor has been paid.
    total_paid_hours: Optional[str] = None  # Total amount of time the Contractor has been paid for.

@dataclass
class ContractorSkillsContractorSkillsObject(APIModel):
    """Auto-generated model for ContractorSkillsContractorSkillsObject."""
    id: Optional[int] = None  # Unique identifier for the contractor skill object.
    contractor: Optional[ContractorSkillsContractorSkillsObjectContractor] = None  # The contractor this skill is associated with.
    subject: Optional[ContractorSkillsContractorSkillsObjectSubject] = None  # The subject details.
    qual_level: Optional[ContractorSkillsContractorSkillsObjectQualLevel] = None  # The qualification level details.

@dataclass
class ContractorSkillsContractorSkillsObjectContractor(APIModel):
    """Auto-generated model for ContractorSkillsContractorSkillsObjectContractor."""
    id: Optional[int] = None  # Unique identifier for the contractor.
    first_name: Optional[str] = None  # The contractor's first name.
    last_name: Optional[str] = None  # The contractor's last name.
    email: Optional[str] = None  # The contractor's email address.
    url: Optional[str] = None  # API URL for the full contractor details.

@dataclass
class ContractorSkillsContractorSkillsObjectSubject(APIModel):
    """Auto-generated model for ContractorSkillsContractorSkillsObjectSubject."""
    id: Optional[int] = None  # Unique identifier for the subject.
    name: Optional[str] = None  # Name of the subject.
    category_id: Optional[int] = None  # ID of the subject category.
    category_name: Optional[str] = None  # Name of the subject category.
    custom_to_branch: Optional[bool] = None  # Indicates whether the Subject is custom to your Branch (True), or is a default Subject (null).

@dataclass
class ContractorSkillsContractorSkillsObjectQualLevel(APIModel):
    """Auto-generated model for ContractorSkillsContractorSkillsObjectQualLevel."""
    id: Optional[int] = None  # Unique identifier for the qualification level.
    name: Optional[str] = None  # Name of the qualification level.
    ranking: Optional[Decimal] = None  # Numerical ranking of the qualification level.
    custom_to_branch: Optional[bool] = None  # Indicates whether the Qualification Level is custom to your Branch (True), or is a default Qualification Level (null).

@dataclass
class CountriesCountryObject(APIModel):
    """Auto-generated model for CountriesCountryObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # The name of the country.
    abbreviation: Optional[str] = None  # The abbreviation of the country.
    three_letter_iso: Optional[str] = None  # The three-letter ISO code for the country.
    currency: Optional[str] = None  # The currency used in the country; e.g Pounds Sterling (£).
    url: Optional[str] = None  # The URL of the country's object.

@dataclass
class InvoicesInvoiceObject(APIModel):
    """Auto-generated model for InvoicesInvoiceObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    charges: List[InvoicesInvoiceObjectChargesItem] = field(default_factory=list)  # An array of different charges related to the invoice.
    client: Optional[InvoicesInvoiceObjectClient] = None  # Object of the Client on the Invoice.
    date_sent: Optional[str] = None  # Date and time the Invoice was sent to the Client.
    date_void: Optional[str] = None  # Date and time the Invoice was marked as void.
    date_paid: Optional[str] = None  # Date and time the Invoice was marked as paid.
    display_id: Optional[str] = None  # Invoice's unique display name.
    gross: Optional[str] = None  # Invoice's gross amount.
    net: Optional[Decimal] = None  # Invoice's net amount.
    status: Optional[str] = None  # Invoice's status. Choice's are `draft`, `confirmed`, `unpaid`, `payment-pending`, `paid`, `failed`, and `void`.
    still_to_pay: Optional[Decimal] = None  # Amount of the Invoice that still needs to be payed.
    tax: Optional[str] = None  # Invoice's tax amount.

@dataclass
class InvoicesInvoiceObjectChargesItem(APIModel):
    """Auto-generated model for InvoicesInvoiceObjectChargesItem."""
    adhoc_charge: Optional[Dict[str, Any]] = None  # Object that contains information about the Ad Hoc Charge. Attributes in the object are `id`, `description`, `date_occurred`, `category_id`, `category_name`, `client_cost`, `pay_contractor`, `agent_percentage`, and `url`.
    amount: Optional[str] = None  # Amount of the charge.
    appointment: Optional[Dict[str, Any]] = None  # Object that contains information about the Appointment. Attributes in the object are `id`, `start`, `finish`, `topic`, `status`, `url`, it also contains a `service` object.
    date: Optional[str] = None  # Date and time the charge occured.
    payee: Optional[str] = None  # Name of who will recieve the charge amount.
    payer: Optional[Dict[str, Any]] = None  # Object of the Client who will pay invoice. Attributes in the object are `id`, `first_name`, `last_name`, `email`, and `url`.
    rate: Optional[str] = None  # The rate used to calculate the charge amount.
    sales_code: Optional[str] = None  # The sales code used for this charge.
    tax_amount: Optional[str] = None  # The amount of tax for this charge.
    units: Optional[str] = None  # Amount of units used to calculate the charge amount.

@dataclass
class InvoicesInvoiceObjectClient(APIModel):
    """Auto-generated model for InvoicesInvoiceObjectClient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Client's object.

@dataclass
class LabelsLabelObject(APIModel):
    """Auto-generated model for LabelsLabelObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # The name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.
    colour: Optional[str] = None  # The colour of the label.
    applicable_role_types: Optional[str] = None  # The role types the label is applicable to.
    email_recipients: Optional[Dict[str, Any]] = None  # The email recipients for the label.
    contractor_editable: Optional[bool] = None  # Whether the label is editable by contractors.
    url: Optional[str] = None  # URL to the label's object.

@dataclass
class NoteNoteObject(APIModel):
    """Auto-generated model for NoteNoteObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    dt_created: Optional[str] = None  # The date the Note was created.
    dt_updated: Optional[str] = None  # The date the Note was last updated.
    creator: Optional[NoteNoteObjectCreator] = None  # The creator of the Note.
    text: Optional[str] = None  # The text of the Note.
    focus: Optional[Dict[str, Any]] = None  # Details about the object the Note was added to.

@dataclass
class NoteNoteObjectCreator(APIModel):
    """Auto-generated model for NoteNoteObjectCreator."""
    id: Optional[int] = None  # The ID of the note creator.
    first_name: Optional[str] = None  # The first name of the note creator.
    last_name: Optional[str] = None  # The last name of the note creator.
    email: Optional[str] = None  # The email address of the note creator.

@dataclass
class PaymentOrdersPaymentOrderObject(APIModel):
    """Auto-generated model for PaymentOrdersPaymentOrderObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    charges: List[PaymentOrdersPaymentOrderObjectChargesItem] = field(default_factory=list)  # An array of different charges related to the payment order.
    payee: Optional[PaymentOrdersPaymentOrderObjectPayee] = None  # Object of the Contractor/Agent on the Payment Order.
    date_sent: Optional[str] = None  # Date and time the Payment Order was sent to the Contractor/Agent.
    date_void: Optional[str] = None  # Date and time the Payment Order was marked as void.
    date_paid: Optional[str] = None  # Date and time the Payment Order was marked as paid.
    display_id: Optional[str] = None  # Payment Order's unique display name.
    amount: Optional[Decimal] = None  # Payment Order's amount.
    status: Optional[str] = None  # Payment Order's status. Choice's are `draft`, `confirmed`, `unpaid`, `payment-pending`, `paid`, `failed`, and `void`.
    still_to_pay: Optional[Decimal] = None  # Amount of the Payment Order that still needs to be payed.
    tax: Optional[str] = None  # Payment Order's tax amount.

@dataclass
class PaymentOrdersPaymentOrderObjectChargesItem(APIModel):
    """Auto-generated model for PaymentOrdersPaymentOrderObjectChargesItem."""
    adhoc_charge: Optional[Dict[str, Any]] = None  # Object that contains information about the Ad Hoc Charge. Attributes in the object are `id`, `description`, `date_occurred`, `category_id`, `category_name`, `client_cost`, `pay_contractor`, `agent_percentage`, and `url`.
    amount: Optional[str] = None  # Amount of the charge.
    appointment: Optional[Dict[str, Any]] = None  # Object that contains information about the Appointment. Attributes in the object are `id`, `start`, `finish`, `topic`, `status`, `url` and `service` object.
    date: Optional[str] = None  # Date and time the charge occured.
    payee: Optional[str] = None  # Object of the Contractor/Agent who will get paid. Attributes in the object are `id`, `first_name`, `last_name`, `email`, and `url`.
    payer: Optional[Dict[str, Any]] = None  # Name of the branch that will be paying the invoice
    rate: Optional[str] = None  # The rate used to calculate the charge amount.
    sales_code: Optional[str] = None  # The sales code used for this charge.
    tax_amount: Optional[str] = None  # The amount of tax for this charge.
    units: Optional[str] = None  # Amount of units used to calculate the charge amount.

@dataclass
class PaymentOrdersPaymentOrderObjectPayee(APIModel):
    """Auto-generated model for PaymentOrdersPaymentOrderObjectPayee."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Contractor/Agent's object.

@dataclass
class PipelineStagesPipelineStageObject(APIModel):
    """Auto-generated model for PipelineStagesPipelineStageObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # The name of the Pipeline Stage
    sort_index: Optional[int] = None  # The sort index of the Pipeline Stage (describes the order of the Pipeline Stages).

@dataclass
class ProformaInvoicesProformaInvoicesObject(APIModel):
    """Auto-generated model for ProformaInvoicesProformaInvoicesObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    amount: Optional[str] = None  # Amount for the Proforma Invoice.
    client: Optional[ProformaInvoicesProformaInvoicesObjectClient] = None  # Object of the Client on the Proforma Invoice.
    display_id: Optional[str] = None  # Proforma Invoice's unique display name.
    date_sent: Optional[str] = None  # Date and time the Proforma Invoice was sent to the Client.
    date_paid: Optional[str] = None  # Date and time the Proforma Invoice was marked as paid.
    items: List[ProformaInvoicesProformaInvoicesObjectItemsItem] = field(default_factory=list)  # An array of items linked to the Proforma Invoice.
    service_recipients: List[ProformaInvoicesProformaInvoicesObjectServiceRecipientsItem] = field(default_factory=list)  # An array of Recipient objects on the Proforma Invoice.
    status: Optional[str] = None  # Proforma Invoice's status. Choice's are `draft`, `confirmed`, `unpaid`, `payment-pending`, `paid`, `failed`, and `void`.
    still_to_pay: Optional[Decimal] = None  # Amount of the Proforma Invoice that still needs to be payed.
    description: Optional[str] = None  # Description for the Proforma Invoice item (required for creation).
    send_pfi: Optional[bool] = None  # (Deprecated - use raise_behaviour instead) Send the PFI as well as creating it. Default is false.
    raise_behaviour: Optional[str] = None  # Raise behavior when creating a Proforma Invoice. Choices are `dont-raise` (default), `raise`, or `raise-and-send`.  If `dont-raise` is used, the PFI will be created but not sent. If `raise` is used, the PFI will be created and staged.  If `raise-and-send` is used, the PFI will be created, staged, and sent to the client.

@dataclass
class ProformaInvoicesProformaInvoicesObjectClient(APIModel):
    """Auto-generated model for ProformaInvoicesProformaInvoicesObjectClient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Client's object.

@dataclass
class ProformaInvoicesProformaInvoicesObjectItemsItem(APIModel):
    """Auto-generated model for ProformaInvoicesProformaInvoicesObjectItemsItem."""
    amount: Optional[str] = None  # Amount for the item.
    custom_description: Optional[str] = None  # Description for the item.
    sales_codes: Optional[str] = None  # Unique identifier for the sales code object used.
    rcra: Optional[Dict[str, Any]] = None  # Object for a linked Recipient on an Appointment. Object containes attributes `recipient`, `recipient_name`, `paying_client`, `paying_client_name`, and `charge_rate`.

@dataclass
class ProformaInvoicesProformaInvoicesObjectServiceRecipientsItem(APIModel):
    """Auto-generated model for ProformaInvoicesProformaInvoicesObjectServiceRecipientsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Recipient's object.

@dataclass
class PublicContractorsPublicContractorObject(APIModel):
    """Auto-generated model for PublicContractorsPublicContractorObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    deleted: Optional[bool] = None  # If the Contractor is deleted or not.
    first_name: Optional[str] = None  # Contractor's first name.
    last_name: Optional[str] = None  # Contractor's last name.
    town: Optional[str] = None  # Contractor's town.
    country: Optional[str] = None  # Contractor's country.
    review_rating: Optional[Decimal] = None  # Contractor's rating.
    review_duration: Optional[int] = None  # Amount of hours that the Contractor has been reviewed for.
    location: Optional[PublicContractorsPublicContractorObjectLocation] = None  # Object contain the Contractor's location.
    photo: Optional[str] = None  # URL to access the Contractor's profile photo.
    extra_attributes: List[Any] = field(default_factory=list)  # An array containing custom field values for the Contractor.
    skills: List[PublicContractorsPublicContractorObjectSkillsItem] = field(default_factory=list)  # An array containing the Contractor's skills.
    labels: List[PublicContractorsPublicContractorObjectLabelsItem] = field(default_factory=list)  # An array of Labels for the Contractor.
    last_updated: Optional[str] = None  # Date and time of when the Contractor was last updated.
    created: Optional[str] = None  # Date and time of when the Contractor was created.
    release_timestamp: Optional[str] = None  # Date and time of when the Contractor's Profile was released.

@dataclass
class PublicContractorsPublicContractorObjectLocation(APIModel):
    """Auto-generated model for PublicContractorsPublicContractorObjectLocation."""
    latitude: Optional[Decimal] = None  # Location's latitude.
    longitude: Optional[Decimal] = None  # Location's longitude.

@dataclass
class PublicContractorsPublicContractorObjectSkillsItem(APIModel):
    """Auto-generated model for PublicContractorsPublicContractorObjectSkillsItem."""
    subject: Optional[str] = None  # Name of the Subject.
    category: Optional[str] = None  # Name of the Subject Category.
    qual_level: Optional[str] = None  # Name of the Qualification Level.
    subject_id: Optional[int] = None  # Unique identifier for the Subject.
    qual_level_id: Optional[int] = None  # Unique identifier for the Qualification Level.
    qual_level_ranking: Optional[Decimal] = None  # Rank for the Qualification Level.

@dataclass
class PublicContractorsPublicContractorObjectLabelsItem(APIModel):
    """Auto-generated model for PublicContractorsPublicContractorObjectLabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class QualLevelQualificationLevelObject(APIModel):
    """Auto-generated model for QualLevelQualificationLevelObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name for the Qualification Level.
    ranking: Optional[Decimal] = None  # Rank for the Qualification Level.
    custom_to_branch: Optional[bool] = None  # Indicates whether the Qualification Level is specific to the your Branch (True), or is a default Qualification Level (null).

@dataclass
class RecipientsRecipientObjectVersion1(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion1."""
    id: Optional[int] = None  # Unique identifier for the object.
    user: Optional[RecipientsRecipientObjectVersion1User] = None  # User object containing basic information.
    default_rate: Optional[Decimal] = None  # The Recipient's default rate.
    paying_client: Optional[RecipientsRecipientObjectVersion1PayingClient] = None  # An object of the Client who pays invoice on behalf of the Recipient.
    associated_clients: List[RecipientsRecipientObjectVersion1AssociatedClientsItem] = field(default_factory=list)  # An array of other Clients associated to this Recipient.
    academic_year: Optional[str] = None  # Name of the academic year the Recipient is in.
    last_updated: Optional[str] = None  # The date and time the Agent was last updated.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[RecipientsRecipientObjectVersion1LabelsItem] = field(default_factory=list)  # An array of the Agent's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`

@dataclass
class RecipientsRecipientObjectVersion1User(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion1User."""
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.

@dataclass
class RecipientsRecipientObjectVersion1PayingClient(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion1PayingClient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class RecipientsRecipientObjectVersion1AssociatedClientsItem(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion1AssociatedClientsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class RecipientsRecipientObjectVersion1LabelsItem(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion1LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class RecipientsRecipientObjectVersion2(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion2."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # The user's first name.
    last_name: Optional[str] = None  # The user's last name.
    email: Optional[str] = None  # The user's email address.
    mobile: Optional[str] = None  # The user's mobile number.
    phone: Optional[str] = None  # The user's phone number.
    street: Optional[str] = None  # The user's street address.
    state: Optional[str] = None  # This field is only needed for US users. This value will use the state's 2-letter code.
    town: Optional[str] = None  # The user's town on address.
    country: Optional[int] = None  # User's country, value is an `id` of the country stored in TutorCruncher. These country ids can be found by doing an options request at this endpoints base URL.
    postcode: Optional[str] = None  # The user's postcode on address.
    latitude: Optional[Decimal] = None  # The user's addresses latitude.
    longitude: Optional[Decimal] = None  # The user's addresses longitude.
    date_created: Optional[str] = None  # The date and time the user was created.
    timezone: Optional[str] = None  # The user's timezone, accepted values are timezone database values.
    photo: Optional[str] = None  # The URL to the Recipient's photo.
    default_rate: Optional[Decimal] = None  # The Recipient's default rate.
    paying_client: Optional[RecipientsRecipientObjectVersion2PayingClient] = None  # An object of the Client who pays invoice on behalf of the Recipient.
    associated_clients: List[RecipientsRecipientObjectVersion2AssociatedClientsItem] = field(default_factory=list)  # An array of other Clients associated to this Recipient.
    academic_year: Optional[str] = None  # Name of the academic year the Recipient is in.
    last_updated: Optional[str] = None  # The date and time the Agent was last updated.
    calendar_colour: Optional[str] = None  # Use hex values, like `#fff000`, or use CSS Named colours.
    labels: List[RecipientsRecipientObjectVersion2LabelsItem] = field(default_factory=list)  # An array of the Agent's labels.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`

@dataclass
class RecipientsRecipientObjectVersion2PayingClient(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion2PayingClient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class RecipientsRecipientObjectVersion2AssociatedClientsItem(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion2AssociatedClientsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Agent's object.

@dataclass
class RecipientsRecipientObjectVersion2LabelsItem(APIModel):
    """Auto-generated model for RecipientsRecipientObjectVersion2LabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class ReportsReportsObject(APIModel):
    """Auto-generated model for ReportsReportsObject."""
    appointment: Optional[ReportsReportsObjectAppointment] = None  # Object of Appointment related to the Report.
    approved: Optional[bool] = None  # If the Report has been approved or not.
    client: Optional[ReportsReportsObjectClient] = None  # Object of the Client related to the Report.
    creator: Optional[ReportsReportsObjectCreator] = None  # Object of the Contractor or Administrator who wrote the Report.
    dt_created: Optional[str] = None  # Date and time when the Report was created.
    extra_attrs: List[ReportsReportsObjectExtraAttrsItem] = field(default_factory=list)  # An array of the Report's extra fields.
    service_recipient: Optional[ReportsReportsObjectServiceRecipient] = None  # Object of the Service recipient related to the Report.

@dataclass
class ReportsReportsObjectAppointment(APIModel):
    """Auto-generated model for ReportsReportsObjectAppointment."""
    id: Optional[int] = None  # Unique identifier for the object.
    finish: Optional[str] = None  # Appointment's finish date and time.
    start: Optional[str] = None  # Appointment's start date and time.
    topic: Optional[str] = None  # Appointment's topic.
    status: Optional[str] = None  # The status for the Appointment, the status types are `planned`, `awaiting-report`, `complete`, `cancelled`, and `cancelled-chargeable`.
    url: Optional[str] = None  # URL to the Appointment's object.
    service: Optional[ReportsReportsObjectAppointmentService] = None  # The Service the Appointment is in.

@dataclass
class ReportsReportsObjectAppointmentService(APIModel):
    """Auto-generated model for ReportsReportsObjectAppointmentService."""
    id: Optional[int] = None  # Unique identifier for the object.
    created: Optional[str] = None  # Date and time when the Service was created.
    dft_charge_type: Optional[str] = None  # How the Service's Appointments will be charged. Types are `hourly` or `one-off`.
    dft_charge_rate: Optional[Decimal] = None  # Defaut charge rate for all Appointments on the Service.
    dft_contractor_rate: Optional[Decimal] = None  # Default Contractor rate for all Appointments on the Service.
    last_updated: Optional[str] = None  # The last time the Service was updated.
    name: Optional[str] = None  # The name of the Service.
    status: Optional[str] = None  # Service's status, choices are `pending`, `available`, `in-progress`, `finished`, and `gone-cold'`.
    url: Optional[str] = None  # URL to the Service's object.

@dataclass
class ReportsReportsObjectClient(APIModel):
    """Auto-generated model for ReportsReportsObjectClient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Client's object.

@dataclass
class ReportsReportsObjectCreator(APIModel):
    """Auto-generated model for ReportsReportsObjectCreator."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Contractor or Administrator object.

@dataclass
class ReportsReportsObjectExtraAttrsItem(APIModel):
    """Auto-generated model for ReportsReportsObjectExtraAttrsItem."""
    id: Optional[int] = None  # Unique identifier for the field's object.
    machine_name: Optional[str] = None  # Unique slugified name of the field.
    name: Optional[str] = None  # The name of the field.
    type: Optional[str] = None  # The type of the field.
    value: Optional[str] = None  # The value of the field.

@dataclass
class ReportsReportsObjectServiceRecipient(APIModel):
    """Auto-generated model for ReportsReportsObjectServiceRecipient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Service recipient's object.

@dataclass
class ReviewsReviewsObject(APIModel):
    """Auto-generated model for ReviewsReviewsObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    client: Optional[ReviewsReviewsObjectClient] = None  # Object of the Client who wrote the Review.
    contractor: Optional[ReviewsReviewsObjectContractor] = None  # Object of the Contractor the Review is for.
    invoice: Optional[ReviewsReviewsObjectInvoice] = None  # Object of the related Invoice.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`
    appointments_duration: Optional[str] = None  # Total hours added up for related Appointments.
    date_created: Optional[str] = None  # Date and time the Review was created.

@dataclass
class ReviewsReviewsObjectClient(APIModel):
    """Auto-generated model for ReviewsReviewsObjectClient."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Client's object.

@dataclass
class ReviewsReviewsObjectContractor(APIModel):
    """Auto-generated model for ReviewsReviewsObjectContractor."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Contractor's object.

@dataclass
class ReviewsReviewsObjectInvoice(APIModel):
    """Auto-generated model for ReviewsReviewsObjectInvoice."""
    id: Optional[int] = None  # Unique identifier for the object.
    accounting_id: Optional[int] = None  # Invoice number.

@dataclass
class WellbeingConcernsSafeguardingWellbeingConcernObject(APIModel):
    """Auto-generated model for WellbeingConcernsSafeguardingWellbeingConcernObject."""
    id: Optional[int] = None  # Unique identifier for the Safeguarding/Wellbeing Concern.
    display_name: Optional[str] = None  # The display name for the Safeguarding/Wellbeing Concern.
    status: Optional[str] = None  # The status of the Safeguarding/Wellbeing Concern.
    severity: Optional[str] = None  # The severity of the Safeguarding/Wellbeing Concern.
    dt_raised: Optional[str] = None  # The date the Safeguarding/Wellbeing Concern was raised.
    dt_resolved: Optional[str] = None  # The date the Safeguarding/Wellbeing Concern was resolved.
    creator: Optional[WellbeingConcernsSafeguardingWellbeingConcernObjectCreator] = None  # The Creator of the Safeguarding/Wellbeing Concern.
    service_recipient: Optional[WellbeingConcernsSafeguardingWellbeingConcernObjectServiceRecipient] = None  # The Student related to the Safeguarding/Wellbeing Concern.
    contractor: Optional[WellbeingConcernsSafeguardingWellbeingConcernObjectContractor] = None  # The Tutor related to the Safeguarding/Wellbeing Concern.
    service: Optional[WellbeingConcernsSafeguardingWellbeingConcernObjectService] = None  # The Service the Safeguarding/Wellbeing Concern is related to.
    appointment: Optional[WellbeingConcernsSafeguardingWellbeingConcernObjectAppointment] = None  # The Appointment related to the Safeguarding/Wellbeing Concern.

@dataclass
class WellbeingConcernsSafeguardingWellbeingConcernObjectCreator(APIModel):
    """Auto-generated model for WellbeingConcernsSafeguardingWellbeingConcernObjectCreator."""
    id: Optional[int] = None  # The ID of the Safeguarding/Wellbeing Concern creator.
    first_name: Optional[str] = None  # The first name of the Safeguarding/Wellbeing Concern creator.
    last_name: Optional[str] = None  # The last name of the Safeguarding/Wellbeing Concern creator.
    email: Optional[str] = None  # The email address of the Safeguarding/Wellbeing Concern creator.
    role_type: Optional[str] = None  # The role type of the Safeguarding/Wellbeing Concern creator.

@dataclass
class WellbeingConcernsSafeguardingWellbeingConcernObjectServiceRecipient(APIModel):
    """Auto-generated model for WellbeingConcernsSafeguardingWellbeingConcernObjectServiceRecipient."""
    id: Optional[int] = None  # The ID of the student related to the Safeguarding/Wellbeing Concern.
    first_name: Optional[str] = None  # The first name of the student related to the Safeguarding/Wellbeing Concern.
    last_name: Optional[str] = None  # The last name of the student related to the Safeguarding/Wellbeing Concern.
    email: Optional[str] = None  # The email address of the student related to the Safeguarding/Wellbeing Concern.
    url: Optional[str] = None  # URL to the Student's object.

@dataclass
class WellbeingConcernsSafeguardingWellbeingConcernObjectContractor(APIModel):
    """Auto-generated model for WellbeingConcernsSafeguardingWellbeingConcernObjectContractor."""
    id: Optional[int] = None  # The ID of the tutor related to the Safeguarding/Wellbeing Concern.
    first_name: Optional[str] = None  # The first name of the tutor related to the Safeguarding/Wellbeing Concern.
    last_name: Optional[str] = None  # The last name of the tutor related to the Safeguarding/Wellbeing Concern.
    email: Optional[str] = None  # The email address of the tutor related to the Safeguarding/Wellbeing Concern.
    url: Optional[str] = None  # URL to the Tutor's object.

@dataclass
class WellbeingConcernsSafeguardingWellbeingConcernObjectService(APIModel):
    """Auto-generated model for WellbeingConcernsSafeguardingWellbeingConcernObjectService."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Service's name.
    dft_charge_type: Optional[str] = None  # Service's default charge type. Check out [Service Object](#service-object) for the types of choices.
    created: Optional[str] = None  # Date and time the Service was created.
    dft_charge_rate: Optional[str] = None  # Service's default amount Clients will be charged.
    dft_contractor_rate: Optional[str] = None  # Service's default amount Contractors will be paided.
    status: Optional[str] = None  # Status of the Service. Check out [Service Object](#service-object) for the types of statuses.
    url: Optional[str] = None  # URL to the Service object.

@dataclass
class WellbeingConcernsSafeguardingWellbeingConcernObjectAppointment(APIModel):
    """Auto-generated model for WellbeingConcernsSafeguardingWellbeingConcernObjectAppointment."""
    id: Optional[int] = None  # Unique identifier for the object.
    start: Optional[str] = None  # Start date and time for the Appointment.
    finish: Optional[str] = None  # Finish date and time for the Appointment.
    topic: Optional[str] = None  # Topic for the Appointment.
    status: Optional[int] = None  # The status for the Appointment, the status types are `planned`, `awaiting-report`, `complete`, `cancelled`, and `cancelled-chargeable`.
    service: Optional[Dict[str, Any]] = None  # Object that contains information about the Service. Attributes in the object are `id`, `name`,  `dft_charge_type`, `created`, `dft_charge_rate`, `dft_conractor_rate`, `last_updated`, `status`, `url`.
    url: Optional[str] = None  # URL to the Appointment object.

@dataclass
class ServicesServiceObject(APIModel):
    """Auto-generated model for ServicesServiceObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    allow_proposed_rates: Optional[bool] = None  # Whether Contractors can propose a rate when applying.
    branch: Optional[int] = None  # Your unique identifier for your Branch.
    branch_tax_setup: Optional[str] = None  # Tax setup for the Branch when invoicing.
    cap: Optional[int] = None  # The maximum number of Appointments that are allowed to occur on the Service.
    colour: Optional[str] = None  # The Service's calendar colour.
    conjobs: List[ServicesServiceObjectConjobsItem] = field(default_factory=list)  # An array of Contractors on the Service.
    contractor_tax_setup: Optional[str] = None  # Tax setup for the Contractors when invoicing.
    created: Optional[str] = None  # Date and time when the Service was created.
    description: Optional[str] = None  # Service's description.
    dft_charge_type: Optional[str] = None  # How the Service's Appointments will be charged. Types are `hourly` or `one-off`.
    dft_charge_rate: Optional[Decimal] = None  # Defaut charge rate for all Appointments on the Service.
    dft_contractor_permissions: Optional[str] = None  # Default Contractor permissions to use for all Contractor's on the Service. Choices are `add-edit-complete`, `add-edit`, `edit`, and `complete`.
    dft_contractor_rate: Optional[Decimal] = None  # Default Contractor rate for all Appointments on the Service.
    dft_location: Optional[ServicesServiceObjectDftLocation] = None  # Object of the Service's Default Location.
    dft_max_srs: Optional[int] = None  # Maximum number of Recipients of allowed on the Service.
    extra_attrs: List[Any] = field(default_factory=list)  # Custom fields for this object.  Updated with payload shape: `'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'}`
    extra_fee_per_apt: Optional[str] = None  # A fixed amount that will be added for each completed Lesson.
    inactivity_time: Optional[int] = None  # Amount of inactive days before the Service will go cold.
    is_bookable: Optional[bool] = None  # Whether Clients can book Recipients onto the Service.
    is_deleted: Optional[bool] = None  # Whether the Service has been deleted.
    labels: List[ServicesServiceObjectLabelsItem] = field(default_factory=list)  # Labels on the Service.
    latest_apt_ahc: Optional[str] = None  # Date and time of the latest Appointment or Ad Hoc Charge is added to Service.
    name: Optional[str] = None  # Service's name.
    net_gross: Optional[str] = None  # Whether the Service Appointments are `net` or `gross`.
    rcrs: List[ServicesServiceObjectRcrsItem] = field(default_factory=list)  # An array of Recipients on the Service.
    require_con_job: Optional[bool] = None  # Whether the Service must have a Contractor to go ahead.
    require_rcr: Optional[bool] = None  # Whether the Service must have a Recipient to go ahead.
    review_units: Optional[int] = None  # The default amount of hours before an automatic review request is sent.
    sales_codes: Optional[int] = None  # Unique identifier of the sales code.
    sr_premium: Optional[str] = None  # An extra amount paid to each Tutor per Student per unit (eg. hour).
    status: Optional[str] = None  # Service's status, choices are `pending`, `available`, `in-progress`, `finished`, and `gone-cold'`.
    total_apt_units: Optional[Decimal] = None  # Total amount of Appointments on the Service, excludes deleted and only cancelled Appointments.

@dataclass
class ServicesServiceObjectConjobsItem(APIModel):
    """Auto-generated model for ServicesServiceObjectConjobsItem."""
    contractor: Optional[int] = None  # Contractor's unique identifier.
    contractor_permissions: Optional[str] = None  # Contractor's permissions on the Service.
    name: Optional[str] = None  # Contractor's full name.
    pay_rate: Optional[Decimal] = None  # A custom pay rate for the Contractor on this Service only.

@dataclass
class ServicesServiceObjectDftLocation(APIModel):
    """Auto-generated model for ServicesServiceObjectDftLocation."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Location's name.
    description: Optional[str] = None  # Location's description.
    can_conflict: Optional[bool] = None  # Whether the location can conflict with other Appointment's at similar time.
    role: Optional[int] = None  # Unique identifier of the related User to the location.
    latitute: Optional[str] = None  # Location's latitude.
    longitude: Optional[str] = None  # Location's longitude.
    address: Optional[str] = None  # Location's full address.

@dataclass
class ServicesServiceObjectLabelsItem(APIModel):
    """Auto-generated model for ServicesServiceObjectLabelsItem."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the label.
    machine_name: Optional[str] = None  # Unique slugified name of the label.

@dataclass
class ServicesServiceObjectRcrsItem(APIModel):
    """Auto-generated model for ServicesServiceObjectRcrsItem."""
    recipient: Optional[int] = None  # Unique identifier of the Recipient.
    recipient_name: Optional[str] = None  # Name of the recipient.
    paying_client: Optional[int] = None  # Unique identifier of the Paying Client for the Recipient.
    paying_client_name: Optional[str] = None  # Name of the Paying Client.
    charge_rate: Optional[str] = None  # Amount the Client will be charged.
    agent: Optional[int] = None  # Unique identifier for the Agent.
    agent_name: Optional[str] = None  # Name of the Agent.
    agent_percentage: Optional[str] = None  # The Agent's percentage on the Service.

@dataclass
class SubjectsSubjectObject(APIModel):
    """Auto-generated model for SubjectsSubjectObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the Subject.
    category_id: Optional[int] = None  # Unique identifier for the Subject's Category.
    category_name: Optional[str] = None  # Name of the Subject's Category.
    custom_to_branch: Optional[bool] = None  # Indicates whether the Subject is specific to your Branch (True), or is a default subject (null).

@dataclass
class SubjectCategoriesSubjectCategoryObject(APIModel):
    """Auto-generated model for SubjectCategoriesSubjectCategoryObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Name of the subject category.

@dataclass
class TasksTaskObject(APIModel):
    """Auto-generated model for TasksTaskObject."""
    id: Optional[int] = None  # Unique identifier for the object.
    admin: Optional[TasksTaskObjectAdmin] = None  # The admin responsible for the Task.
    complete: Optional[bool] = None  # Whether or not the Task is completed.
    description: Optional[str] = None  # The description of the Task.
    due_dt: Optional[str] = None  # The date the Task is due.
    notification_pending: Optional[bool] = None  # Whether or not a reminder is still to be sent.
    reminder_dt: Optional[str] = None  # The date the reminder is to be sent.
    repeater: Optional[str] = None  # How often the Task is to be repeated, the two choices are `weekly` or `monthly`.
    repeat_every: Optional[str] = None  # Repeat every x weeks or months.
    role: Optional[TasksTaskObjectRole] = None  # Object of the Role.
    service: Optional[TasksTaskObjectService] = None  # Object of the Service.
    task_type: Optional[str] = None  # The type of Task, the options are `phone`, `email`, `service-cold` or `other`.

@dataclass
class TasksTaskObjectAdmin(APIModel):
    """Auto-generated model for TasksTaskObjectAdmin."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # The users first name.
    last_name: Optional[str] = None  # The users last name.
    email: Optional[str] = None  # The users email address.

@dataclass
class TasksTaskObjectRole(APIModel):
    """Auto-generated model for TasksTaskObjectRole."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # The users first name.
    last_name: Optional[str] = None  # The users last name.
    email: Optional[str] = None  # The users email address.
    url: Optional[str] = None  # URL to the Role's object.

@dataclass
class TasksTaskObjectService(APIModel):
    """Auto-generated model for TasksTaskObjectService."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # The name of the Service.
    dft_charge_type: Optional[str] = None  # The default charge type of the Service.
    created: Optional[str] = None  # The date the Service was created.
    dft_charge_rate: Optional[str] = None  # The default charge rate of the Service.
    dft_contractor_rate: Optional[str] = None  # The default contractor rate of the Service.
    last_updated: Optional[str] = None  # The date the Service was last updated.
    status: Optional[str] = None  # The status of the Service.
    url: Optional[str] = None  # URL to the Service's object.

@dataclass
class TendersTenderObject(APIModel):
    """Auto-generated model for TendersTenderObject."""
    description: Optional[str] = None  # Tender's description from the Contractor.
    contractor: Optional[TendersTenderObjectContractor] = None  # Object of the Contractor who is applying.
    created: Optional[str] = None  # Date and time the Tender object was created.
    proposed_rate: Optional[str] = None  # Proposed rate from the Contractor when they applied.
    service: Optional[TendersTenderObjectService] = None  # Object of the Service the Contractor applied for.
    status: Optional[str] = None  # Tender's status, choices are `pending`, `requested`, `accepted`, `rejected`, and `withdrawn`.

@dataclass
class TendersTenderObjectContractor(APIModel):
    """Auto-generated model for TendersTenderObjectContractor."""
    id: Optional[int] = None  # Unique identifier for the object.
    first_name: Optional[str] = None  # User's first name.
    last_name: Optional[str] = None  # User's last name.
    email: Optional[str] = None  # User's email address.
    url: Optional[str] = None  # URL to the Contractor's object.

@dataclass
class TendersTenderObjectService(APIModel):
    """Auto-generated model for TendersTenderObjectService."""
    id: Optional[int] = None  # Unique identifier for the object.
    name: Optional[str] = None  # Service's name.
    dft_charge_type: Optional[str] = None  # Service's default charge type. Check out [Service Object](#service-object) for the types of choices.
    created: Optional[str] = None  # Date and time the Service was created.
    dft_charge_rate: Optional[str] = None  # Service's default amount Clients will be charged.
    dft_contractor_rate: Optional[str] = None  # Service's default amount Contractors will be paided.
    status: Optional[str] = None  # Status of the Service. Check out [Service Object](#service-object) for the types of statuses.
    url: Optional[str] = None  # URL to the Service object.

@dataclass
class AgentsAgentObjectVersion1Filters(APIModel):
    """Filter parameters for AgentsAgentObjectVersion1Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Agent was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Agent was created.
    user_first_name: Optional[str] = None  # Filter by the Agent's first name.
    user_last_name: Optional[str] = None  # Filter by the Agent's last name.
    user_email: Optional[str] = None  # Filter by the Agent's email address.
    status: Optional[str] = None  # Filter by the Agent's status.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Agent's labels (id).

@dataclass
class AgentsAgentObjectVersion2Filters(APIModel):
    """Filter parameters for AgentsAgentObjectVersion2Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Agent was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Agent was created.
    user_first_name: Optional[str] = None  # Filter by the Agent's first name.
    user_last_name: Optional[str] = None  # Filter by the Agent's last name.
    user_email: Optional[str] = None  # Filter by the Agent's email address.
    status: Optional[str] = None  # Filter by the Agent's status.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Agent's labels (id).

@dataclass
class AppointmentsAppointmentObjectFilters(APIModel):
    """Filter parameters for AppointmentsAppointmentObjectFilters."""
    start_gte: Optional[str] = None  # Filter by the date and time the Appointment was started.
    start_lte: Optional[str] = None  # Filter by the date and time the Appointment was ended.
    service: Optional[int] = None  # Filter by the Appointment's linked Job (id).
    contractor: Optional[int] = None  # Filter by the Appointment's linked Tutor (id).
    recipient: Optional[int] = None  # Filter by the Appointment's linked Student (id).
    client: Optional[int] = None  # Filter by the Appointment's linked Client (id).
    status: Optional[str] = None  # Filter by the Appointment's status (string).
    location: Optional[int] = None  # Filter by the Appointment's location (id).

@dataclass
class BalanceUpdatesBalanceUpdateObjectFilters(APIModel):
    """Filter parameters for BalanceUpdatesBalanceUpdateObjectFilters."""
    client: Optional[int] = None  # Filter by the Balance Updates linked Client (id).
    contractor: Optional[int] = None  # Filter by the Balance Updates linked Tutor (id).
    method: Optional[str] = None  # Filter by the Balance Updates method. Options for this field are ['cash', 'cheque', 'credit_card', 'transferwise', 'debit_card', 'bank_transfer', 'direct_debit', 'bonus_credit', 'manual', 'voucher', 'correction']'
    update_type: Optional[str] = None  # Filter by the Balance Updates update_type. Options for this field are ['proforma_invoice_paid', 'invoice_creation', 'invoice_payment', 'po_creation', 'po_payment', 'adjustment', 'refund', 'stripe_bank_transfer_refund', 'voucher', 'credit_note', 'debit_note', 'via_api', 'top_up', 'app_fee']'
    credit_amount_gte: Optional[Decimal] = None  # Filter by Balance Updates with a credit_amount greater than or equal to this value.
    credit_amount_lte: Optional[Decimal] = None  # Filter by Balance Updates with a credit_amount less than or equal to this value.
    created_gte: Optional[datetime] = None  # Filter by Balance Updates created on or after this date and time.
    created_lte: Optional[datetime] = None  # Filter by Balance Updates created on or before this date and time.

@dataclass
class ClientsClientObjectVersion1Filters(APIModel):
    """Filter parameters for ClientsClientObjectVersion1Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Client was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Client was created.
    user_first_name: Optional[str] = None  # Filter by the Client's first name.
    user_last_name: Optional[str] = None  # Filter by the Client's last name.
    user_email: Optional[str] = None  # Filter by the Client's email address.
    status: Optional[str] = None  # Filter by the Client's status.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Client's labels (id).

@dataclass
class ClientsClientObjectVersion2Filters(APIModel):
    """Filter parameters for ClientsClientObjectVersion2Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Client was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Client was created.
    user_first_name: Optional[str] = None  # Filter by the Client's first name.
    user_last_name: Optional[str] = None  # Filter by the Client's last name.
    user_email: Optional[str] = None  # Filter by the Client's email address.
    status: Optional[str] = None  # Filter by the Client's status.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Client's labels (id).

@dataclass
class ContractorsContractorObjectVersion1Filters(APIModel):
    """Filter parameters for ContractorsContractorObjectVersion1Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Contractor was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Contractor was created.
    user_first_name: Optional[str] = None  # Filter by the Contractor's first name.
    user_last_name: Optional[str] = None  # Filter by the Contractor's last name.
    user_email: Optional[str] = None  # Filter by the Contractor's email address.
    status: Optional[str] = None  # Filter by the Contractor's status.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Contractor's labels (id).
    skills: Optional[int] = None  # Filter by the Contractor's skills (id).

@dataclass
class ContractorsContractorObjectVersion2Filters(APIModel):
    """Filter parameters for ContractorsContractorObjectVersion2Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Contractor was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Contractor was created.
    user_first_name: Optional[str] = None  # Filter by the Contractor's first name.
    user_last_name: Optional[str] = None  # Filter by the Contractor's last name.
    user_email: Optional[str] = None  # Filter by the Contractor's email address.
    status: Optional[str] = None  # Filter by the Contractor's status.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Contractor's labels (id).
    skills: Optional[int] = None  # Filter by the Contractor's skills (id).

@dataclass
class PublicContractorsPublicContractorObjectFilters(APIModel):
    """Filter parameters for PublicContractorsPublicContractorObjectFilters."""
    release_gte: Optional[str] = None  # Filter by the date and time the Agent was released.
    release_lte: Optional[str] = None  # Filter by the date and time the Agent was released.

@dataclass
class RecipientsRecipientObjectVersion1Filters(APIModel):
    """Filter parameters for RecipientsRecipientObjectVersion1Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Recipient was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Recipient was created.
    user_first_name: Optional[str] = None  # Filter by the Recipient's first name.
    user_last_name: Optional[str] = None  # Filter by the Recipient's last name.
    user_email: Optional[str] = None  # Filter by the Recipient's email address.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Recipient's labels (id).

@dataclass
class RecipientsRecipientObjectVersion2Filters(APIModel):
    """Filter parameters for RecipientsRecipientObjectVersion2Filters."""
    user_created_gte: Optional[str] = None  # Filter by the date and time the Recipient was created.
    user_created_lte: Optional[str] = None  # Filter by the date and time the Recipient was created.
    user_first_name: Optional[str] = None  # Filter by the Recipient's first name.
    user_last_name: Optional[str] = None  # Filter by the Recipient's last name.
    user_email: Optional[str] = None  # Filter by the Recipient's email address.
    distance_address: Optional[str] = None  # Filter by the address.
    distance_radius: Optional[int] = None  # Filter by the radius of the address. This is used in conjunction with the `address` filter.
    labels: Optional[int] = None  # Filter by the Recipient's labels (id).

@dataclass
class ReportsReportsObjectFilters(APIModel):
    """Filter parameters for ReportsReportsObjectFilters."""
    dt_created_gte: Optional[Any] = None  # Filter by the date and time the report was created.
    dt_created_lte: Optional[Any] = None  # Filter by the date and time the report was created.
    appointment: Optional[int] = None  # Filter reports by specific Appointment
    creator: Optional[int] = None  # Filter reports by User who created the report
    service_recipient: Optional[int] = None  # Filter reports by specific Service recipient
    client: Optional[int] = None  # Filter reports by specific Client

@dataclass
class ServicesServiceObjectFilters(APIModel):
    """Filter parameters for ServicesServiceObjectFilters."""
    created_gte: Optional[str] = None  # Filter by the date and time the Service was created.
    created_lte: Optional[str] = None  # Filter by the date and time the Service was created.
    last_updated_gte: Optional[str] = None  # Filter by the date and time the Service was updated.
    last_updated_lte: Optional[str] = None  # Filter by the date and time the Service was updated.
    labels: Optional[int] = None  # Filter by the Service's labels (id).

@dataclass
class TendersTenderObjectFilters(APIModel):
    """Filter parameters for TendersTenderObjectFilters."""
    contractor: Optional[int] = None  # Filter by the Contractor's id.
    service: Optional[int] = None  # Filter by the Service's id.
    created_gte: Optional[str] = None  # Filter by the date and time the Tender was created.
    created_lte: Optional[str] = None  # Filter by the date and time the Tender was created.

__all__ = ['AdhocchargesAdHocChargeObject', 'AdhocchargesAdHocChargeObjectAgent', 'AdhocchargesAdHocChargeObjectAppointment', 'AdhocchargesAdHocChargeObjectCategory', 'AdhocchargesAdHocChargeObjectClient', 'AdhocchargesAdHocChargeObjectContractor', 'AdhocchargesAdHocChargeObjectCreator', 'AdhocchargesAdHocChargeObjectInvoicesItem', 'AdhocchargesAdHocChargeObjectPaymentOrdersItem', 'AdhocchargesAdHocChargeObjectService', 'AhcCategoriesAdHocChargeCategoryObject', 'AgentsAgentObjectVersion1', 'AgentsAgentObjectVersion1User', 'AgentsAgentObjectVersion1ClientsItem', 'AgentsAgentObjectVersion1LabelsItem', 'AgentsAgentObjectVersion2', 'AgentsAgentObjectVersion2ClientsItem', 'AgentsAgentObjectVersion2LabelsItem', 'AppointmentsAppointmentObject', 'AppointmentsAppointmentObjectLocation', 'AppointmentsAppointmentObjectRcrasItem', 'AppointmentsAppointmentObjectCjasItem', 'AppointmentsAppointmentObjectRepeater', 'BalanceUpdatesBalanceUpdateObject', 'BalanceUpdatesBalanceUpdateObjectCreator', 'BalanceUpdatesBalanceUpdateObjectRole', 'BranchBranchObject', 'BranchBranchObjectAgency', 'BranchBranchObjectDatetimeOutputFormats', 'ClientsClientObjectVersion1', 'ClientsClientObjectVersion1User', 'ClientsClientObjectVersion1AssociatedAdmin', 'ClientsClientObjectVersion1AssociatedAgent', 'ClientsClientObjectVersion1PipelineStage', 'ClientsClientObjectVersion1PaidRecipientsItem', 'ClientsClientObjectVersion1LabelsItem', 'ClientsClientObjectVersion2', 'ClientsClientObjectVersion2AssociatedAdmin', 'ClientsClientObjectVersion2AssociatedAgent', 'ClientsClientObjectVersion2PipelineStage', 'ClientsClientObjectVersion2PaidRecipientsItem', 'ClientsClientObjectVersion2LabelsItem', 'ContractorsContractorObjectVersion1', 'ContractorsContractorObjectVersion1User', 'ContractorsContractorObjectVersion1QualificationsItem', 'ContractorsContractorObjectVersion1SkillsItem', 'ContractorsContractorObjectVersion1InstitutionsItem', 'ContractorsContractorObjectVersion1LabelsItem', 'ContractorsContractorObjectVersion1WorkDoneDetails', 'ContractorsContractorObjectVersion2', 'ContractorsContractorObjectVersion2QualificationsItem', 'ContractorsContractorObjectVersion2SkillsItem', 'ContractorsContractorObjectVersion2InstitutionsItem', 'ContractorsContractorObjectVersion2LabelsItem', 'ContractorsContractorObjectVersion2WorkDoneDetails', 'ContractorSkillsContractorSkillsObject', 'ContractorSkillsContractorSkillsObjectContractor', 'ContractorSkillsContractorSkillsObjectSubject', 'ContractorSkillsContractorSkillsObjectQualLevel', 'CountriesCountryObject', 'InvoicesInvoiceObject', 'InvoicesInvoiceObjectChargesItem', 'InvoicesInvoiceObjectClient', 'LabelsLabelObject', 'NoteNoteObject', 'NoteNoteObjectCreator', 'PaymentOrdersPaymentOrderObject', 'PaymentOrdersPaymentOrderObjectChargesItem', 'PaymentOrdersPaymentOrderObjectPayee', 'PipelineStagesPipelineStageObject', 'ProformaInvoicesProformaInvoicesObject', 'ProformaInvoicesProformaInvoicesObjectClient', 'ProformaInvoicesProformaInvoicesObjectItemsItem', 'ProformaInvoicesProformaInvoicesObjectServiceRecipientsItem', 'PublicContractorsPublicContractorObject', 'PublicContractorsPublicContractorObjectLocation', 'PublicContractorsPublicContractorObjectSkillsItem', 'PublicContractorsPublicContractorObjectLabelsItem', 'QualLevelQualificationLevelObject', 'RecipientsRecipientObjectVersion1', 'RecipientsRecipientObjectVersion1User', 'RecipientsRecipientObjectVersion1PayingClient', 'RecipientsRecipientObjectVersion1AssociatedClientsItem', 'RecipientsRecipientObjectVersion1LabelsItem', 'RecipientsRecipientObjectVersion2', 'RecipientsRecipientObjectVersion2PayingClient', 'RecipientsRecipientObjectVersion2AssociatedClientsItem', 'RecipientsRecipientObjectVersion2LabelsItem', 'ReportsReportsObject', 'ReportsReportsObjectAppointment', 'ReportsReportsObjectAppointmentService', 'ReportsReportsObjectClient', 'ReportsReportsObjectCreator', 'ReportsReportsObjectExtraAttrsItem', 'ReportsReportsObjectServiceRecipient', 'ReviewsReviewsObject', 'ReviewsReviewsObjectClient', 'ReviewsReviewsObjectContractor', 'ReviewsReviewsObjectInvoice', 'WellbeingConcernsSafeguardingWellbeingConcernObject', 'WellbeingConcernsSafeguardingWellbeingConcernObjectCreator', 'WellbeingConcernsSafeguardingWellbeingConcernObjectServiceRecipient', 'WellbeingConcernsSafeguardingWellbeingConcernObjectContractor', 'WellbeingConcernsSafeguardingWellbeingConcernObjectService', 'WellbeingConcernsSafeguardingWellbeingConcernObjectAppointment', 'ServicesServiceObject', 'ServicesServiceObjectConjobsItem', 'ServicesServiceObjectDftLocation', 'ServicesServiceObjectLabelsItem', 'ServicesServiceObjectRcrsItem', 'SubjectsSubjectObject', 'SubjectCategoriesSubjectCategoryObject', 'TasksTaskObject', 'TasksTaskObjectAdmin', 'TasksTaskObjectRole', 'TasksTaskObjectService', 'TendersTenderObject', 'TendersTenderObjectContractor', 'TendersTenderObjectService', 'AgentsAgentObjectVersion1Filters', 'AgentsAgentObjectVersion2Filters', 'AppointmentsAppointmentObjectFilters', 'BalanceUpdatesBalanceUpdateObjectFilters', 'ClientsClientObjectVersion1Filters', 'ClientsClientObjectVersion2Filters', 'ContractorsContractorObjectVersion1Filters', 'ContractorsContractorObjectVersion2Filters', 'PublicContractorsPublicContractorObjectFilters', 'RecipientsRecipientObjectVersion1Filters', 'RecipientsRecipientObjectVersion2Filters', 'ReportsReportsObjectFilters', 'ServicesServiceObjectFilters', 'TendersTenderObjectFilters']
